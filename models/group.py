from models import tasks_groups_table
from store.postgres import sa


class Group(sa.Model):
    __tablename__ = "groups"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=False)
    user = sa.relationship(
        "User",
        back_populates="groups",
    )
    tasks = sa.relationship(
        "Task",
        secondary=tasks_groups_table,
        back_populates="groups",
        cascade="save-update, merge, delete"
    )

    @staticmethod
    def get_by_id(group_id):
        group = sa.session.query(Group).filter_by(id=group_id).first()
        return group

    @staticmethod
    def create_group(group_name: str, user_id: int):
        group = Group(name=group_name, user_id=user_id)
        sa.session.add(group)
        return group

    @staticmethod
    def get_users_groups(user_id: int):
        groups = sa.session.query(Group).filter_by(user_id=user_id).all()
        return groups

    @staticmethod
    def delete_group(group_id: int):
        print(f"Удаляем группу {group_id}")
        group = Group.get_by_id(group_id)
        sa.session.delete(group)
        print(f"Удалили группу {group_id}")
