import asyncio
import os

from dotenv import load_dotenv
from speechmatics.rt import (
    AsyncClient,
    AudioEncoding,
    AudioFormat,
    AuthenticationError,
    Microphone,
    OperatingPoint,
    ServerMessageType,
    TranscriptResult,
    TranscriptionConfig,
)

load_dotenv()


async def transcribe_microphone() -> str:
    api_key = os.getenv("SPEECHMATICS_API_KEY")

    if not api_key:
        raise RuntimeError(
            "SPEECHMATICS_API_KEY is not configured."
        )

    audio_format = AudioFormat(
        encoding=AudioEncoding.PCM_S16LE,
        chunk_size=4096,
        sample_rate=16000,
    )

    transcription_config = TranscriptionConfig(
        language="en",
        enable_partials=True,
        operating_point=OperatingPoint.ENHANCED,
    )

    mic = Microphone(
      device_index=5,
      sample_rate=audio_format.sample_rate,
      chunk_size=audio_format.chunk_size,
    )

    transcript_parts: list[str] = []

    if not mic.start():
        raise RuntimeError(
            "Microphone could not start. "
            "Make sure PyAudio is installed."
        )

    try:
        async with AsyncClient(api_key=api_key) as client:

            @client.on(ServerMessageType.ADD_TRANSCRIPT)
            def handle_final_transcript(message):
                result = TranscriptResult.from_message(message)
                transcript = result.metadata.transcript

                if transcript:
                    print(f"[final] {transcript}")
                    transcript_parts.append(transcript)

            @client.on(ServerMessageType.ADD_PARTIAL_TRANSCRIPT)
            def handle_partial_transcript(message):
                result = TranscriptResult.from_message(message)
                transcript = result.metadata.transcript

                if transcript:
                    print(f"[partial] {transcript}")

            await client.start_session(
                transcription_config=transcription_config,
                audio_format=audio_format,
            )

            print("🎤 Listening...")
            print("Speak your packing instruction.")
            print("Press Ctrl+C to stop.\n")

            while True:
                frame = await mic.read(
                    audio_format.chunk_size
                )

                await client.send_audio(frame)

    except KeyboardInterrupt:
        print("\nStopping microphone...")

    except (AuthenticationError, ValueError) as exc:
        raise RuntimeError(
            f"Speechmatics error: {exc}"
        ) from exc

    finally:
        mic.stop()

    return " ".join(transcript_parts).strip()


async def main():
    transcript = await transcribe_microphone()

    print("\nFinal transcript:")
    print(transcript)


if __name__ == "__main__":
    asyncio.run(main())