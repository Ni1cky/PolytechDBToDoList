from models import tasks_groups_table, Subtask
from store.postgres import sa


class Task(sa.Model):
    __tablename__ = "tasks"
    id = sa.Column(sa.Integer, primary_key=True)
    description = sa.Column(sa.String)
    complete = sa.Column(sa.Boolean)
    groups = sa.relationship(
        "Group",
        secondary=tasks_groups_table,
        back_populates="tasks",
    )
    deadline = sa.relationship(
        "Deadline",
        back_populates="task",
        cascade="save-update, merge, delete"
    )

    @staticmethod
    def set_complete(task_id: int):
        task = sa.session.query(Task).filter_by(id=task_id).first()
        task.complete = not task.complete
        sa.session.add(task)

    @staticmethod
    def create_task(description: str):
        new_task = Task(
            description=description, complete=False
        )
        sa.session.add(new_task)
        return new_task

    def get_subtasks(self):
        subtasks_ids = sa.session.query(Subtask).with_entities(Subtask.subtask_id).filter_by(main_id=self.id).all()
        subtasks_ids = [subtask[0] for subtask in subtasks_ids]
        subtasks = [
            sa.session.query(Task).filter_by(id=task_id).first()
            for task_id in subtasks_ids
        ]
        return subtasks

    def delete_subtasks(self):
        subtasks = self.get_subtasks()
        for subtask in subtasks:
            sa.session.delete(subtask)
        subtasks_connection_columns = sa.session.query(Subtask).filter_by(main_id=self.id).all()
        for subtask_connection_column in subtasks_connection_columns:
            sa.session.delete(subtask_connection_column)

    @staticmethod
    def delete_task(task_id: int):
        task = sa.session.query(Task).filter_by(id=task_id).first()
        task.delete_subtasks()
        sa.session.delete(task)
