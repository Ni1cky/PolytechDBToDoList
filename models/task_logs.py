from store.postgres import sa


class TaskLogs(sa.Model):
    __tablename__ = "tasks_logs"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    task_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"))
    creation_date = sa.Column(sa.Date)
    finish_date = sa.Column(sa.Date)
    task = sa.relationship(
        "Task",
        back_populates="logs",
    )
