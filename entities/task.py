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
        return []  # TODO: Получение списка задач в выбранной группе
