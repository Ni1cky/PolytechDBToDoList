from flask import Blueprint, session, redirect, url_for, request

from entities import Group

groups_blueprint = Blueprint("group", __name__)


@groups_blueprint.route("/group", methods=["POST"])
def add_new_group():
    if session.get("user", None):
        parameters = request.form.to_dict()
        new_group_name = parameters["new_group_name"]
        Group.create_group(new_group_name)
    return redirect(url_for("views.home"))
