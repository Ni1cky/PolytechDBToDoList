from store.postgres import sa


class Block(sa.Model):
    __tablename__ = "blocks"
    id = sa.Column(sa.Integer, primary_key=True)
    blocked_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"))
    blocking_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"))
