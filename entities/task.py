from flask import session
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    description: str
    user_id: int

    class Config:
        orm_mode = True

    @staticmethod
    def get_groups_tasks(current_group_id: int):
        current_user = session["user"]
        return [{'id': 1, 'description': 'банан', 'user_id': 1, 'subtasks': [{'id': 1, 'description': 'подбанан'}, {'id': 2, 'description': 'подподбанан'}]},
                {'id': 2, 'description': 'ананас', 'user_id': 1},
                {'id': 3, 'description': 'водород', 'user_id': 1}]  # TODO: Получение списка задач в выбранной группе