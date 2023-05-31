from hashlib import sha256

from flask import Blueprint, request, redirect, flash, url_for, session

from entities import User
from routers.validation import validate_text_field

login_blueprint = Blueprint("login", __name__)


@login_blueprint.route("/login", methods=["POST"])
def login():
    parameters = request.form.to_dict()
    email = parameters["email"]
    password = parameters["password"]
    if validate_text_field(password):
        password_hash = sha256(password.encode()).hexdigest()

        if parameters["sign"] == "up":
            if User.get_by_email(email):
                flash("Такой аккаунт уже существует!")
            else:
                User.create_user(email, password_hash)
        else:
            if User.check_auth(email, password_hash):
                return redirect(url_for("views.home"))
            flash("Неправильная почта или пароль!")
    else:
        flash("Введите пароль!")
    return redirect(url_for("views.home"))


@login_blueprint.route("/logout")
def logout():
    if "user" in session:
        session.pop("user")
    if "current_group_id" in session:
        session.pop("current_group_id")
    return redirect(url_for("views.home"))
