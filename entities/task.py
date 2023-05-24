from datetime import date
from typing import Optional

from pydantic import BaseModel

from models import Group


class Task(BaseModel):
    id: int
    description: str
    complete: bool
    subtasks: Optional[list]
    dead_line: Optional[date]

    class Config:
        orm_mode = True

    @staticmethod
    def get_groups_tasks(group_id: int, to_dicts=False):
        task_models = Group.get_by_id(group_id).tasks
        tasks = []
        for task_model in task_models:
            task = Task.from_orm(task_model)
            if task_model.deadline:
                task.dead_line = task_model.deadline[0].deadline
            subtasks = [
                Task.from_orm(subtask_model)
                for subtask_model in task_model.get_subtasks()
            ]
            if to_dicts:
                subtasks = [subtask.dict() for subtask in subtasks]
            task.subtasks = subtasks
            tasks.append(task)
        if to_dicts:
            tasks = [task.dict() for task in tasks]
        return tasks
