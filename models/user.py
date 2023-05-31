from store.postgres import sa


class User(sa.Model):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    email = sa.Column(sa.String)
    password_hash = sa.Column(sa.String)
    groups = sa.relationship(
        "Group",
        back_populates="user",
        cascade="save-update, merge, delete"
    )

    @staticmethod
    def get_by_email(email: str):
        user = sa.session.query(User).filter_by(email=email).first()
        return user

    @staticmethod
    def create_user(email: str, password_hash: str):
        user = User(email=email, password_hash=password_hash)
        sa.session.add(user)
        return user
