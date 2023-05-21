from hashlib import sha256

from flask import Blueprint, request, redirect, flash, url_for

from entities import User
from models import User as UserModel

login_blueprint = Blueprint("login", __name__)


@login_blueprint.route("/login", methods=["POST"])
def login():
    parameters = request.form.to_dict()
    email = parameters["email"]
    password_hash = sha256(parameters["password"].encode()).hexdigest()

    if parameters["sign"] == "up":
        if User.get_by_email(email):
            flash("Такой аккаунт уже существует!")
        else:
            UserModel.create_user(email, password_hash)
            flash("Вы зарегистрировались! Можно войти")
    else:
        if User.check_auth(email, password_hash):
            return redirect(url_for("views.home"))
        flash("Неправильная почта или пароль!")
    return redirect(url_for("hello"))
