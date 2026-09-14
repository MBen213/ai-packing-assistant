from pydantic import BaseModel
from typing import List, Dict


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
    arm: str = "arm1"


class PackingPlan(BaseModel):
    target: str
    actions: List[PackingAction]