from app.parser import parse_instruction
from app.planner import generate_plan


text = (
    "Pack these items into the box, "
    "keep the fragile item on top, "
    "and place the heavier item at the bottom."
)

instruction = parse_instruction(text)
plan = generate_plan(instruction)

print("\nInstruction:")
print(instruction.model_dump())

print("\nPacking Plan:")
print(plan.model_dump())