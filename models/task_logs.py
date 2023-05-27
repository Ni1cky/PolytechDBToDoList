from datetime import datetime

from store.postgres import sa


class TaskLogs(sa.Model):
    __tablename__ = "tasks_logs"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    task_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"), index=True)
    creation_date = sa.Column(sa.Date)
    finish_date = sa.Column(sa.Date)
    task = sa.relationship(
        "Task",
        back_populates="logs",
    )

    @staticmethod
    def get_by_task_id(task_id: int):
        log = sa.session.query(TaskLogs).filter_by(task_id=task_id).first()
        return log

    @staticmethod
    def log_creation(task_id: int):
        log = TaskLogs(task_id=task_id, creation_date=datetime.today())
        sa.session.add(log)

    @staticmethod
    def log_finish(task_id: int):
        log = TaskLogs.get_by_task_id(task_id)
        log.finish_date = datetime.today()
        sa.session.add(log)
