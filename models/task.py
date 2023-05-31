from datetime import date

from flask import session
from sqlalchemy import or_

from models import tasks_groups_table, TaskLogs, Group
from store.postgres import sa


class Task(sa.Model):
    __tablename__ = "tasks"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    description = sa.Column(sa.String)
    completed = sa.Column(sa.Boolean)
    deadline = sa.Column(sa.Date)
    parent_id = sa.Column(sa.Integer, index=True, nullable=False)
    groups = sa.relationship(
        "Group",
        secondary=tasks_groups_table,
        back_populates="tasks",
    )
    logs = sa.relationship(
        "TaskLogs",
        back_populates="task",
    )

    @staticmethod
    def set_completed(task_id: int):
        task = sa.session.query(Task).filter_by(id=task_id).first()
        task.completed = True
        sa.session.add(task)
        TaskLogs.log_finish(task_id)

        if task.parent_id:
            parent = Task.get_by_id(task.parent_id)
            parent.check_subtasks_completion()

    @staticmethod
    def get_by_id(task_id: int):
        task = sa.session.query(Task).filter_by(id=task_id).first()
        return task

    @staticmethod
    def create_task(description: str, parent_id=0):
        new_task = Task(
            description=description, completed=False, parent_id=parent_id
        )
        sa.session.add(new_task)
        sa.session.commit()
        TaskLogs.log_creation(new_task.id)
        return new_task

    def get_subtasks(self):
        subtasks = sa.session.query(Task).filter_by(parent_id=self.id).all()
        return subtasks

    def delete_subtasks(self):
        subtasks = self.get_subtasks()
        for subtask in subtasks:
            sa.session.delete(subtask)

    @staticmethod
    def delete_task(task_id: int):
        task = sa.session.query(Task).filter_by(id=task_id).first()
        if not task.completed:
            task.delete_subtasks()
            sa.session.delete(task)

    @staticmethod
    def set_deadline_by_id(task_id: int, deadline: date):
        task = sa.session.query(Task).filter_by(id=task_id).first()
        if not task.completed:
            task.deadline = deadline
            sa.session.add(task)

    def check_subtasks_completion(self):
        subtasks = self.get_subtasks()
        if all([subtask.completed for subtask in subtasks]):
            self.completed = True
            sa.session.add(self)

    @staticmethod
    def get_statistics():
        all_group_id = sa.session.query(Group).filter_by(
            name="Все задачи", user_id=session["user"]["id"]
        ).first().id

        tasks_with_stats_query = sa.session.query(
            Task.id, Task.description, Task.deadline, Task.parent_id, Task.completed,
            TaskLogs.creation_date, TaskLogs.finish_date
        ).join(tasks_groups_table).filter_by(
            group_id=all_group_id
        ).filter(
            or_(Task.completed == True, Task.parent_id != 0)
        ).join(TaskLogs).filter(
            TaskLogs.task_id == Task.id
        )
        print(tasks_with_stats_query)
        tasks_with_logs = tasks_with_stats_query.all()

        formatted_result = list()
        for task in tasks_with_logs:
            if task.parent_id == 0:
                formatted_result.append(
                    {
                        "description": task.description,
                        "deadline": task.deadline,
                        "creation_date": task.creation_date,
                        "finish_date": task.finish_date,
                        "subtasks": [
                            {
                                "description": subtask.description,
                                "completed": subtask.completed,
                                "creation_date": subtask.creation_date,
                                "finish_date": subtask.finish_date
                            }
                            for subtask in tasks_with_logs
                            if subtask.parent_id == task.id
                        ]
                    }
                )
        return formatted_result
