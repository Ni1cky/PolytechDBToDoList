import hashlib

from flask import session

from store.postgres import sa


class User(sa.Model):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String)
    password_hash = sa.Column(sa.String)

    @staticmethod
    def get_user_by_email(email: str):
        user = sa.session.query(User).filter_by(email=email).first()
        return user

    @staticmethod
    def check_auth(email: str, password_hash: str):
        user = User.get_user_by_email(email)
        if user and password_hash == user.password_hash:
            session["user"] = user.id
            return True
        return False
