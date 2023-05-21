from flask import session
from pydantic import BaseModel
from models import User as UserModel


class Task(BaseModel):
    id: int
    description: str
    user_id: int

    class Config:
        orm_mode = True

    @staticmethod
    def get_groups_tasks(current_group: str):
        current_user = session["user"]
        return []  # TODO: Получение списка задач в выбранной группе
