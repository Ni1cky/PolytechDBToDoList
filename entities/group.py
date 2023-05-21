from flask import session
from pydantic import BaseModel
from models import Group as GroupModel


class Group(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        orm_mode = True

    @staticmethod
    def get_by_id(group_id: int):
        group_model = GroupModel.get_by_id(group_id)
        group = Group.from_orm(group_model)
        return group

    @staticmethod
    def get_users_groups(user_id: int = None, to_dicts=False):
        user_id = user_id if user_id else session["user"]["id"]
        group_models = GroupModel.get_users_groups(user_id)
        groups = [Group.from_orm(group) for group in group_models]
        if to_dicts:
            groups = [group.dict() for group in groups]
        return groups
