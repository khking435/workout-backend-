"""Rename tables to Users, Workouts, Userworkouts

Revision ID: d1c1308938dc
Revises: 7dfeba3cf21a
Create Date: 2024-07-14 10:17:38.375909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1c1308938dc'
down_revision = '7dfeba3cf21a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('sets', sa.Integer(), nullable=False),
    sa.Column('reps', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['workout_id'], ['Workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Userworkouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['Workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('exercise')
    op.drop_table('UserWorkout')
    op.drop_table('Workout')
    op.drop_table('User')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('password', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Workout',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('date', sa.DATE(), nullable=False),
    sa.Column('duration', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('UserWorkout',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('workout_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['Workout.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('workout_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('sets', sa.INTEGER(), nullable=False),
    sa.Column('reps', sa.INTEGER(), nullable=False),
    sa.Column('weight', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['workout_id'], ['Workout.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Userworkouts')
    op.drop_table('Exercises')
    op.drop_table('Workouts')
    op.drop_table('Users')
    # ### end Alembic commands ###
