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

    actions = [
        PackingAction(
            object_type="heavy",
            position=positions["heavy"],
            action_type="bimanual_pick_place",
            arms=["arm1", "arm2"],
        ),
        PackingAction(
            object_type="normal",
            position=positions["normal"],
            action_type="pick_place",
            arms=["arm1"],
        ),
        PackingAction(
            object_type="fragile",
            position=positions["fragile"],
            action_type="pick_place",
            arms=["arm2"],
        ),
    ]

    return PackingPlan(
        target=instruction.target,
        actions=actions,
    )