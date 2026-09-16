# 🤖 Intelligent Packing Assistant

An intelligent robotic packing assistant developed by **Team 15** for the **AI Infra Summit Hackathon 2026**.

The project demonstrates how a natural-language packing instruction can be transformed into a structured packing plan and then executed through a **Three.js robotic simulation**, including coordinated **bimanual manipulation** for the Heavy object.

The project was built for the:

**Intel Bimanual VLA Manipulation with Multi-Modal Reasoning**

---

## 🚀 Project Overview

The **Intelligent Packing Assistant** receives a natural-language packing instruction, extracts packing constraints, generates structured robot actions, and sends the resulting plan to a Three.js simulation.

### Current Prototype Flow

```text
Natural-Language Instruction
            ↓
       FastAPI /plan
            ↓
   Instruction Parsing
            ↓
      Packing Planner
            ↓
   Structured Robot Actions
            ↓
      Three.js Simulator
            ↓
   Bimanual Execution
            ↓
     Final Verification
```

The current prototype focuses on an end-to-end planning and simulation workflow for a controlled packing scenario.

---

## 📦 MVP Scenario

The MVP uses:

* 1 Heavy object
* 1 Normal object
* 1 Fragile object
* 1 box
* 2 robotic arms

### Example Instruction

```text
Pack these items into the box, keep the fragile item on top,
and place the heavier item at the bottom.
```

### Expected Arrangement

```text
Heavy   → Bottom
Normal  → Middle
Fragile → Top
```

### Generated Execution Plan

```text
Heavy   → Bottom → Arm 1 + Arm 2
Normal  → Middle → Arm 1
Fragile → Top → Arm 2
```

The Heavy object uses a coordinated **bimanual pick-and-place** action involving both robotic arms.

---

## 🧠 Backend API

The backend is implemented with **FastAPI** and exposes a public `/plan` endpoint.

### Live API

https://ai-packing-assistant.onrender.com

### Swagger Documentation

https://ai-packing-assistant.onrender.com/docs

### Endpoint

```text
POST /plan
```

### Request

```json
{
  "text": "Pack these items into the box, keep the fragile item on top, and place the heavier item at the bottom."
}
```

### Example Response

```json
{
  "instruction": {
    "target": "box",
    "constraints": {
      "heavy": "bottom",
      "normal": null,
      "fragile": "top"
    }
  },
  "plan": {
    "target": "box",
    "actions": [
      {
        "object_type": "heavy",
        "position": "bottom",
        "action_type": "bimanual_pick_place",
        "arms": [
          "arm1",
          "arm2"
        ]
      },
      {
        "object_type": "normal",
        "position": "middle",
        "action_type": "pick_place",
        "arms": [
          "arm1"
        ]
      },
      {
        "object_type": "fragile",
        "position": "top",
        "action_type": "pick_place",
        "arms": [
          "arm2"
        ]
      }
    ]
  },
  "order": [
    "Heavy",
    "Normal",
    "Fragile"
  ]
}
```

The API returns both the high-level packing order and explicit robotic actions, including the arms assigned to each object.

---

## 🧩 Instruction Parsing

The current instruction parser uses a **rule-based approach** to identify supported packing constraints.

For the current MVP, it extracts relationships such as:

```text
Heavy   → Bottom
Fragile → Top
Normal  → Middle
```

The parser is intentionally lightweight and designed for the controlled hackathon scenario.

It can be extended later with more advanced language understanding or multimodal reasoning.

---

## 🎮 Three.js Robotic Simulator

The simulator is located at:

```text
simulator/index.html
```

It connects to the deployed FastAPI backend, receives the generated plan, and visualizes the robot execution.

### Current Integration Flow

```text
User Instruction
       ↓
JavaScript fetch()
       ↓
FastAPI /plan
       ↓
Structured Packing Plan
       ↓
data.order + data.plan.actions
       ↓
runPacking()
       ↓
Three.js Robotic Simulation
```

### Bimanual Execution

The simulator reads the action assignments returned by the backend.

For the Heavy object:

```json
{
  "object_type": "heavy",
  "position": "bottom",
  "action_type": "bimanual_pick_place",
  "arms": [
    "arm1",
    "arm2"
  ]
}
```

Both robotic arms participate in the manipulation and move with the Heavy object during the transport and placement sequence.

The simulation maintains the object and assigned arms together during the bimanual movement before releasing the object at the final position.

---

## ✅ Final-State Verification

After the packing sequence completes, the simulator performs a final-state verification step.

The verification checks that the objects are positioned according to the expected packing arrangement.

The successful state is reported as:

```text
Packing complete — final arrangement verified.
```

This provides a basic validation layer after robot execution.

---

## 🎙️ Speechmatics Integration

A local microphone pipeline is included using **Speechmatics Realtime**.

The implementation is located at:

```text
app/speech.py
```

The prototype performs real-time speech-to-text using the Speechmatics SDK.

### Local Audio Dependencies

Speech-related microphone dependencies are kept separate from the Render deployment:

```text
requirements-local.txt
```

This allows the microphone pipeline to be tested locally without requiring audio hardware dependencies in the cloud deployment.

### Current Voice Pipeline

```text
Microphone
    ↓
Speechmatics Realtime
    ↓
Speech Transcript
    ↓
Natural-Language Instruction
```

The current Speechmatics component is a **local speech-to-text prototype** and is not yet directly embedded into the deployed web simulator.

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* python-dotenv
* Speechmatics Realtime SDK

### Frontend / Simulation

* HTML5
* JavaScript
* Three.js
* GSAP

### Development & Deployment

* Git
* GitHub
* Render
* REST API
* Swagger / OpenAPI

---

## 📁 Project Structure

```text
ai-packing-assistant/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── parser.py
│   ├── planner.py
│   ├── schemas.py
│   └── speech.py
│
├── simulator/
│   └── index.html
│
├── test_pipeline.py
├── requirements.txt
├── requirements-local.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/MBen213/ai-packing-assistant.git
cd ai-packing-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install backend dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the FastAPI application

```bash
python -m uvicorn app.main:app --reload
```

### 6. Open API documentation

```text
http://127.0.0.1:8000/docs
```

---

## 🎮 Run the Simulator

From the project directory:

```powershell
python -m http.server 5500 --directory simulator
```

Then open:

```text
http://localhost:5500
```

The simulator communicates with the deployed planning API and visualizes the generated packing actions.

---

## 🎙️ Run the Local Speechmatics Prototype

Install the local dependencies:

```powershell
pip install -r requirements-local.txt
```

Then run:

```powershell
python app\speech.py
```

The Speechmatics prototype listens to microphone input and produces real-time transcripts.

A valid Speechmatics API key must be configured through the project's environment configuration.

---

## 🧪 Testing

The current planning pipeline can be tested with:

```bash
python test_pipeline.py
```

### Current Test Flow

```text
Natural-Language Instruction
            ↓
     Instruction Parser
            ↓
       Packing Planner
            ↓
   Structured Robot Actions
            ↓
      Packing Order
```

The hackathon validation process also covers:

* Basic packing
* Heavy-at-bottom constraint
* Fragile-at-top constraint
* End-to-end planning
* Bimanual coordination
* Final-state verification

---

## 🔄 Current End-to-End Prototype

The current implemented prototype is:

```text
Natural-Language Instruction
            ↓
      Instruction Parser
            ↓
       Packing Planner
            ↓
      FastAPI /plan
            ↓
   Structured Robot Actions
            ↓
      Three.js Simulator
            ↓
     Bimanual Execution
            ↓
     Final Verification
```

A separate local Speechmatics prototype provides:

```text
Microphone
    ↓
Speechmatics
    ↓
Speech-to-Text
```

The voice pipeline and robotic simulation are currently separate components of the prototype.

---

## 🔮 Roadmap

Future development can extend the current prototype with:

* Fully integrated voice-to-robot web workflow
* More advanced multimodal object understanding
* Vision-based object detection
* Richer natural-language reasoning
* Dynamic replanning
* Failure recovery
* Automatic recovery after failed placement
* More complex bimanual manipulation scenarios
* Real robot integration
* Advanced final-state perception and verification

---

## 👥 Team 15

### Mohamed Benkhaled — MBen213

* AI/backend integration
* Instruction parsing
* Packing-plan generation
* Robot action planning
* API deployment
* Speechmatics integration
* Simulator integration

### Wessfago

* Simulation environment
* Robotic arms
* Object manipulation
* Bimanual coordination

### Eséchiel

* Task logic
* Test scenarios
* Testing and validation
* Documentation
* Integration support
* Final demo support

Roles may evolve as the project continues.

---

## 🏆 Hackathon

**AI Infra Summit Hackathon 2026**

### Track

**Intel Bimanual VLA Manipulation with Multi-Modal Reasoning**

### Project

**Intelligent Packing Assistant**

### Repository

https://github.com/MBen213/ai-packing-assistant

### Live API

https://ai-packing-assistant.onrender.com

### API Documentation

https://ai-packing-assistant.onrender.com/docs

---

## 📌 Project Status

### Current Status

**MVP implemented and deployed 🚀**

The project currently provides:

* Natural-language instruction parsing
* Structured packing-plan generation
* Public FastAPI deployment
* API-to-simulator integration
* Three.js robotic simulation
* Coordinated bimanual manipulation
* Final-state verification
* Local Speechmatics speech-to-text prototype

### Current MVP Milestone

```text
Natural Language
      ↓
Instruction Parsing
      ↓
Packing Planner
      ↓
FastAPI
      ↓
Robot Actions
      ↓
Three.js Simulation
      ↓
Bimanual Execution
      ↓
Final Verification
```

---

## 🔗 Project Links

* **GitHub Repository:** https://github.com/MBen213/ai-packing-assistant
* **Live API:** https://ai-packing-assistant.onrender.com
* **Swagger Documentation:** https://ai-packing-assistant.onrender.com/docs

---

## 🚀 Built by Team 15

**AI Infra Summit Hackathon 2026**

**Intel Bimanual VLA Manipulation with Multi-Modal Reasoning**

Built with Python, FastAPI, Speechmatics, JavaScript, Three.js, and GSAP.
