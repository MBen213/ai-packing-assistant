# 🤖 Intelligent Packing Assistant

An intelligent robotic packing assistant developed for the **AI Infra Summit Hackathon 2026**.

The project explores natural-language instruction understanding, packing-plan generation, and robotic simulation for the:

**Intel Bimanual VLA Manipulation with Multi-Modal Reasoning**

---

## 🚀 Project Overview

The Intelligent Packing Assistant receives a natural-language packing instruction, extracts the relevant packing constraints, generates a structured packing plan, and sends the resulting packing order to a Three.js robotic simulation.

### Current Prototype Flow

```text
Natural-Language Instruction
            ↓
      FastAPI /plan API
            ↓
    Instruction Parsing
            ↓
      Packing Planner
            ↓
  Structured Packing Plan
            ↓
      Packing Order
            ↓
    Three.js Simulator

📦 Current MVP

The current prototype supports:

Natural-language packing instructions
Packing constraint extraction
Instruction parsing
Structured packing-plan generation
FastAPI backend
Public API deployment on Render
Three.js robotic simulation
AI/API → Simulator integration
Example Instruction
Pack these items into the box, keep the fragile item on top,
and place the heavier item at the bottom.
Generated Packing Order
[
  "Heavy",
  "Normal",
  "Fragile"
]

The simulator uses this order to animate the packing sequence.

🧠 API
Base URL

https://ai-packing-assistant.onrender.com

Swagger Documentation

https://ai-packing-assistant.onrender.com/docs

Endpoint
POST /plan

The /plan endpoint receives a natural-language packing instruction and returns:

Interpreted packing constraints
A structured packing plan
The execution order
Example Request
{
  "text": "Pack these items into the box, keep the fragile item on top, and place the heavier item at the bottom."
}
Example Response
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
        "arm": "arm1"
      },
      {
        "object_type": "normal",
        "position": "middle",
        "arm": "arm1"
      },
      {
        "object_type": "fragile",
        "position": "top",
        "arm": "arm1"
      }
    ]
  },
  "order": [
    "Heavy",
    "Normal",
    "Fragile"
  ]
}

🎮 Three.js Simulator

The simulator is located at:

simulator/index.html

The simulator sends a natural-language instruction to the public API and passes the returned packing order to:

runPacking(data.order);

Current Integration Flow

User Instruction
       ↓
JavaScript fetch()
       ↓
FastAPI /plan
       ↓
Structured Packing Plan
       ↓
data.order
       ↓
runPacking(data.order)
       ↓
Three.js Packing Simulation

🛠️ Tech Stack
Backend
Python
FastAPI
Pydantic
Uvicorn
Frontend / Simulation
HTML5
JavaScript
Three.js
GSAP
Deployment
GitHub
Render

📁 Project Structure
ai-packing-assistant/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── parser.py
│   ├── planner.py
│   └── schemas.py
│
├── simulator/
│   └── index.html
│
├── test_pipeline.py
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md

💻 Run Locally
1. Clone the repository
git clone https://github.com/MBen213/ai-packing-assistant.git
cd ai-packing-assistant
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
Windows PowerShell
.\.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Run the API
python -m uvicorn app.main:app --reload
6. Open API documentation
http://127.0.0.1:8000/docs

🧪 Testing

The current packing pipeline can be tested with:

python test_pipeline.py
Current Test Flow
Natural-Language Instruction
            ↓
     Instruction Parser
            ↓
       Packing Planner
            ↓
  Structured Packing Plan
            ↓
["Heavy", "Normal", "Fragile"]

]
🔄 Current End-to-End Prototype

The current prototype demonstrates:

Natural-Language Instruction
            ↓
      Instruction Parser
            ↓
       Packing Planner
            ↓
      FastAPI /plan
            ↓
      Packing Order
            ↓
     Three.js Simulator
            ↓
      Packing Animation

🔮 Roadmap

The planned next development stages are:

 Voice input with Speechmatics
 Speech-to-text integration
 Multimodal object understanding
 Meaningful bimanual robot coordination
 Final-state verification
 End-to-end voice-to-robot demo
 Dynamic replanning
 Automatic recovery

The team is prioritizing the core end-to-end MVP before implementing optional features.

👥 Team 15
Mohamed Benkhaled — MBen213
AI/backend integration
Instruction parsing
Packing-plan generation
Action-plan integration
API deployment
Voice pipeline integration
Wessfago
Simulation environment
Robotic arms
Object manipulation
Bimanual coordination
Eséchiel
Task logic
Test scenarios
Testing and validation
Documentation
Integration support
Final demo support

Roles may be adjusted as additional teammates are integrated.

🏆 Hackathon

AI Infra Summit Hackathon 2026

Track

Intel Bimanual VLA Manipulation with Multi-Modal Reasoning

Repository

https://github.com/MBen213/ai-packing-assistant

Live API

https://ai-packing-assistant.onrender.com

API Documentation

https://ai-packing-assistant.onrender.com/docs

📌 Project Status

MVP Integration in Progress 🚀

The AI planning API is publicly deployed, and the Three.js simulator is being integrated with the API.

Next Major Milestones
Voice Input
    ↓
Speech-to-Text
    ↓
Instruction Understanding
    ↓
Packing Reasoning
    ↓
Bimanual Robot Actions
    ↓
Final-State Verification

🚀 Built by Team 15

AI Infra Summit Hackathon 2026

Intel Bimanual VLA Manipulation with Multi-Modal Reasoning