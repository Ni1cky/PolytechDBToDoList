from store.postgres import sa


class Group(sa.Model):
    __tablename__ = "groups"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    