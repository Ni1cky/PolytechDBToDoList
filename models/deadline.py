from datetime import date

from store.postgres import sa


class Deadline(sa.Model):
    __tablename__ = "deadlines"
    id = sa.Column(sa.Integer, primary_key=True)
    deadline = sa.Column(sa.Date)
    task_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"), nullable=False)
    task = sa.relationship(
        "Task",
        back_populates="deadline"
    )

    @staticmethod
    def set_deadline(task_id: int, deadline_date: date):
        deadline = sa.session.query(Deadline).filter_by(task_id=task_id).first()
        if deadline:
            deadline.deadline = deadline_date
        else:
            deadline = Deadline(deadline=deadline_date, task_id=task_id)
        sa.session.add(deadline)
