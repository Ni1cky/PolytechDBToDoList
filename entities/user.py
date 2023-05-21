from flask import session
from pydantic import BaseModel
from models import User as UserModel


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
