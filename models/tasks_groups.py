from store.postgres import sa


tasks_groups_table = sa.Table(
    "tasks_groups",
    sa.Column("group_id", sa.ForeignKey("groups.id"), primary_key=True, index=True),
    sa.Column("task_id", sa.ForeignKey("tasks.id"), primary_key=True),
)
