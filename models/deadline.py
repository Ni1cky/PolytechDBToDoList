from store.postgres import sa


class Deadline(sa.Model):
    __tablename__ = "deadlines"
    id = sa.Column(sa.Integer, primary_key=True)
    deadline = sa.Column(sa.Date)
    task_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"))
