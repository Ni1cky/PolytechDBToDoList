from store.postgres import sa


class Subtask(sa.Model):
    __tablename__ = "subtasks"
    id = sa.Column(sa.Integer, primary_key=True)
    main_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"), nullable=False)
    subtask_id = sa.Column(sa.Integer, sa.ForeignKey("tasks.id"), nullable=False)

    @staticmethod
    def create_subtask_column(subtask_id: int, main_task_id: int):
        subtask_column = Subtask(main_id=main_task_id, subtask_id=subtask_id)
        sa.session.add(subtask_column)
