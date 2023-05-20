from store.postgres import sa


class TasksGroups(sa.Model):
    __tablename__ = "tasks_groups"
    id = sa.Column(sa.Integer, primary_key=True)
    task_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"))
    group_id = sa.Column(sa.Integer, sa.ForeignKey("groups.id"))
