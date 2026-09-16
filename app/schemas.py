from pydantic import BaseModel
from typing import List


class PackingConstraints(BaseModel):
    heavy: str | None = None
    normal: str | None = None
    fragile: str | None = None


class PackingInstruction(BaseModel):
    target: str
    constraints: PackingConstraints


class PackingAction(BaseModel):
    object_type: str
    position: str
    action_type: str
    arms: List[str]


class PackingPlan(BaseModel):
    target: str
    actions: List[PackingAction]