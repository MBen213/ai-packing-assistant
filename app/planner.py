from app.schemas import PackingInstruction, PackingPlan, PackingAction


DEFAULT_POSITIONS = {
    "heavy": "bottom",
    "normal": "middle",
    "fragile": "top",
}


def generate_plan(instruction: PackingInstruction) -> PackingPlan:
    positions = DEFAULT_POSITIONS.copy()

    if instruction.constraints.heavy:
        positions["heavy"] = instruction.constraints.heavy

    if instruction.constraints.normal:
        positions["normal"] = instruction.constraints.normal

    if instruction.constraints.fragile:
        positions["fragile"] = instruction.constraints.fragile

    order = ["heavy", "normal", "fragile"]

    actions = [
        PackingAction(
            object_type=obj,
            position=positions[obj],
            arm="arm1",
        )
        for obj in order
    ]

    return PackingPlan(
        target=instruction.target,
        actions=actions,
    )