from sqlalchemy import select
from src.models.tasks_model import Tasks
from src.schemas.tasks import TaskAdd
from src.db.db import session_maker


class TasksSevice:

    @staticmethod
    def add_task(data: TaskAdd):
        with session_maker() as session:
            task_info = data.model_dump()
            task = Tasks(**task_info)

            session.add(task)
            session.flush()
            session.commit()

            return task.id


    @staticmethod
    def get_all():
        with session_maker() as session:
            query = select(Tasks)

            res = session.execute(query)
            result = [row[0].to_read_model() for row in res.all()]

            return result
        
