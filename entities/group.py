from flask import session
from pydantic import BaseModel
from models import Group as GroupModel
from store.postgres import sa


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

    @staticmethod
    def create_group(group_name: str, user_id: int = None):
        user_id = user_id if user_id else session["user"]["id"]
        group_model = GroupModel.create_group(group_name, user_id)
        sa.session.commit()
        group = Group.from_orm(group_model)
        return group

    @staticmethod
    def get_all_group():
        current_users_groups = Group.get_users_groups()
        for g in current_users_groups:
            if g.name == "Все задачи":
                return g

    @staticmethod
    def delete_group(group_id: int):
        all_group = Group.get_all_group()
        if all_group.id != group_id:
            GroupModel.delete_group(group_id)
