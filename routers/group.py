from flask import Blueprint, session, redirect, url_for, request

from entities import Group

groups_blueprint = Blueprint("group", __name__)


@groups_blueprint.route("/group", methods=["POST"])
def add_new_group():
    if session.get("user", None):
        parameters = request.form.to_dict()
        new_group_name = parameters["new_group_name"]
        group = Group.create_group(new_group_name)
        return redirect(url_for("views.home", current_group_id=group.id))
    return redirect(url_for("views.home"))


@groups_blueprint.route("/group/delete/<int:group_id>", methods=["POST"])
def delete_group(group_id: int):
    if session.get("user", None):
        Group.delete_group(group_id)
    return redirect(url_for("views.home"))
