from app.schemas import PackingInstruction, PackingConstraints


def parse_instruction(text: str) -> PackingInstruction:
    text_lower = text.lower()

    heavy = None
    normal = None
    fragile = None

    # Heavy → Bottom
    if (
        ("heavy" in text_lower or "heavier" in text_lower)
        and "bottom" in text_lower
    ):
        heavy = "bottom"

    # Normal → Middle
    if "normal" in text_lower and "middle" in text_lower:
        normal = "middle"

    # Fragile → Top
    if "fragile" in text_lower and "top" in text_lower:
        fragile = "top"

    return PackingInstruction(
        target="box",
        constraints=PackingConstraints(
            heavy=heavy,
            normal=normal,
            fragile=fragile,
        ),
    )