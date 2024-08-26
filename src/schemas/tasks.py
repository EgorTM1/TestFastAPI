from pydantic import BaseModel

class TaskAdd(BaseModel):
    name: str
    description: str


class Tasks(BaseModel):
    id: int
    name: str
    description: str

