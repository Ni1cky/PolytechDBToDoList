from store.postgres import sa


class User(sa.Model):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String)
    password_hash = sa.Column(sa.String)
