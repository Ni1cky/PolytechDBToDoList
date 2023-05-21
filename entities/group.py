from flask import session
from pydantic import BaseModel


class Group(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        orm_mode = True

    @staticmethod
    def get_users_groups():
        current_user = session["user"]
        return []  # TODO: Получение списка групп задач юзера
