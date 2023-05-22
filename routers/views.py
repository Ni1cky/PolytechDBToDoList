from flask import Blueprint, session, render_template

from entities import Group, Task

views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/", defaults={"current_group_id": 1})
@views_blueprint.route("/home", defaults={"current_group_id": 1})
@views_blueprint.route("/<int:current_group_id>")
@views_blueprint.route("/home/<int:current_group_id>")
def home(current_group_id: int):
    if session.get("user", None):
        return render_template(
            "home.html",
            groups=Group.get_users_groups(to_dicts=True),
            tasks=Task.get_groups_tasks(current_group_id),
            current_group=Group.get_by_id(current_group_id).dict()
        )
    return render_template("login.html")
