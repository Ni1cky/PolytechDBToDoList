from flask import session
from pydantic import BaseModel

from entities import Group
from models import User as UserModel
from store.postgres import sa


class User(BaseModel):
    id: int
    email: str
    password_hash: str

    class Config:
        orm_mode = True

    @staticmethod
    def get_by_email(email: str):
        user_model = UserModel.get_by_email(email)
        user = User.from_orm(user_model) if user_model else None
        return user

    @staticmethod
    def check_auth(email: str, password_hash: str):
        user = User.get_by_email(email)
        if user and password_hash == user.password_hash:
            session["user"] = user.dict()
            return True
        return False

    @staticmethod
    def create_user(email: str, password_hash: str):
        new_user = UserModel.create_user(email, password_hash)
        sa.session.commit()
        session["user"] = User.from_orm(new_user).dict()
        Group.create_group("Все задачи")
        Group.create_group("Сегодня")
