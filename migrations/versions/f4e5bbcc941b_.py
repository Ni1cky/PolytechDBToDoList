"""empty message

Revision ID: f4e5bbcc941b
Revises: afdc69751773
Create Date: 2023-05-20 18:08:40.450550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4e5bbcc941b'
down_revision = 'afdc69751773'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blocked_id', sa.Integer(), nullable=True),
    sa.Column('blocking_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blocked_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['blocking_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deadlines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subtasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('main_id', sa.Integer(), nullable=True),
    sa.Column('subtask_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['main_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['subtask_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks_groups')
    op.drop_table('subtasks')
    op.drop_table('deadlines')
    op.drop_table('blocks')
    # ### end Alembic commands ###
