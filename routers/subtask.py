from flask import Blueprint, request, redirect, url_for, session

from models import Task, Subtask
from routers.validation import validate_session, validate_text_field
from store.postgres import sa

subtasks_blueprint = Blueprint("subtasks", __name__)


@subtasks_blueprint.route("/subtasks/<int:main_task_id>", methods=["POST"])
def create_subtask(main_task_id: int):
    if validate_session():
        parameters = request.form.to_dict()
        new_subtask_name = parameters["new_subtask_name"]
        if validate_text_field(new_subtask_name):
            subtask = Task.create_task(new_subtask_name)
            sa.session.commit()
            Subtask.create_subtask_column(subtask.id, main_task_id)
    return redirect(url_for("views.home", current_group_id=session["current_group_id"]))


@subtasks_blueprint.route("/subtasks/delete/<int:subtask_id>", methods=["POST"])
def delete_subtask(subtask_id: int):
    Task.delete_task(subtask_id, is_subtask=True)
    return redirect(url_for("views.home", current_group_id=session["current_group_id"]))
