from store.postgres import sa


class Task(sa.Model):
    __tablename__ = "tasks"
    id = sa.Column(sa.Integer, primary_key=True)
    description = sa.Column(sa.String)
    complete = sa.Column(sa.Boolean)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
