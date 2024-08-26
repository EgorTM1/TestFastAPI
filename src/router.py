from typing import List
from fastapi import APIRouter
from src.services.tasks import TasksSevice
from src.schemas.tasks import TaskAdd, Tasks


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)

@router.get('')
def get_all() -> List[Tasks]:
    result = TasksSevice.get_all()

    return result


@router.post('')
def add_task(data: TaskAdd) -> int:
    result = TasksSevice.add_task(data)

    return result
