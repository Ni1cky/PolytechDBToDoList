from hashlib import sha256

from flask import Blueprint, request, redirect, session, flash

from models import User
from store.postgres import sa

login_blueprint = Blueprint("login", __name__)


@login_blueprint.route("/login", methods=["POST"])
def login():
    parameters = request.form.to_dict()
    email = parameters["email"]
    password_hash = sha256(parameters["password"].encode()).hexdigest()

    if parameters["sign"] == "up":
        if User.get_user_by_email(email):
            flash("Такой аккаунт уже существует!")
        else:
            user = User(email=email, password_hash=password_hash)
            sa.session.add(user)
            flash("Вы зарегистрировались! Можно войти")
    else:
        if User.check_auth(email, password_hash):
            return redirect("/home")
        flash("Неправильная почта или пароль!")
    return redirect("/")
