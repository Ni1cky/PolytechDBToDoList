from datetime import date

from flask import Blueprint
from flask_cors import cross_origin

from models import Task, Deadline

tasks_blueprint = Blueprint("task", __name__)


@cross_origin()
@tasks_blueprint.route("/tasks/complete/<int:task_id>", methods=["PUT"])
def complete_task(task_id: int):
    Task.set_complete(task_id)


@cross_origin()
@tasks_blueprint.route("/deadline/<int:task_id>/<deadline>", methods=["PUT"])
def set_deadline(task_id: int, deadline: date):
    Deadline.set_deadline(task_id, deadline)
