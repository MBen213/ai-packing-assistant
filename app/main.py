from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.parser import parse_instruction
from app.planner import generate_plan


app = FastAPI(title="Intelligent Packing Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InstructionRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "message": "Intelligent Packing Assistant API is running"
    }


@app.post("/plan")
def create_packing_plan(request: InstructionRequest):
    instruction = parse_instruction(request.text)
    plan = generate_plan(instruction)

    order = [
        action.object_type.capitalize()
        for action in plan.actions
    ]

    return {
        "instruction": instruction.model_dump(),
        "plan": plan.model_dump(),
        "order": order,
    }