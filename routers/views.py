from flask import Blueprint, render_template, session

from entities import Group, Task
from models import Task as TaskModel
from routers.validation import validate_session

views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/", defaults={"current_group_id": None})
@views_blueprint.route("/home", defaults={"current_group_id": None})
@views_blueprint.route("/<int:current_group_id>")
@views_blueprint.route("/home/<int:current_group_id>")
def home(current_group_id: int):
    if validate_session():
        current_group = (
            Group.get_by_id(current_group_id) if current_group_id
            else Group.get_all_group()
        )
        session["current_group_id"] = current_group.id
        return render_template(
            "home.html",
            groups=Group.get_users_groups(to_dicts=True),
            tasks=Task.get_groups_tasks(current_group.id, to_dicts=True),
            current_group=current_group.dict()
        )
    return render_template("login.html")


@views_blueprint.route("/statistics")
def get_statistics():
    if validate_session():
        statistics = TaskModel.get_statistics()
        return render_template("statistics.html", statistics=statistics)
