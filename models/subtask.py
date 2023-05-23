from store.postgres import sa


class Subtask(sa.Model):
    __tablename__ = "subtasks"
    id = sa.Column(sa.Integer, primary_key=True)
    main_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"), nullable=False)
    subtask_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"), nullable=False)
