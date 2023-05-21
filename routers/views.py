from flask import Blueprint, session, redirect, render_template, url_for

from entities import Group, Task

views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/", defaults={"current_group": "Все"})
@views_blueprint.route("/home", defaults={"current_group": "Все"})
@views_blueprint.route("/<current_group>")
@views_blueprint.route("/home/<current_group>")
def home(current_group):
    if session.get("user", None):
        return render_template(
            "home.html",
            groups=Group.get_users_groups(),
            tasks=Task.get_groups_tasks(current_group),
            current_group=current_group
        )
    return render_template("login.html")
