from models import tasks_groups_table
from store.postgres import sa


class Task(sa.Model):
    __tablename__ = "tasks"
    id = sa.Column(sa.Integer, primary_key=True)
    description = sa.Column(sa.String)
    complete = sa.Column(sa.Boolean)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=False)
    user = sa.relationship(
        "User",
        back_populates="tasks"
    )
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
