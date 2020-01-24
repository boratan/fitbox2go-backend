"""empty message

Revision ID: a9aa7e98c903
Revises: 
Create Date: 2020-01-23 20:02:52.229065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9aa7e98c903'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise_types',
    sa.Column('exercise_type_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('default_reps', sa.Integer(), nullable=True),
    sa.Column('default_series', sa.Integer(), nullable=True),
    sa.Column('default_weight', sa.Float(), nullable=True),
    sa.Column('default_rest', sa.Integer(), nullable=True),
    sa.Column('default_speed', sa.Integer(), nullable=True),
    sa.Column('default_range_of_motion', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('video_link', sa.String(length=128), nullable=True),
    sa.Column('default_leftarmplate_level', sa.Integer(), nullable=True),
    sa.Column('default_rightarmplate_level', sa.Integer(), nullable=True),
    sa.Column('default_middleplate_level', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('exercise_type_id')
    )
    op.create_table('result_types',
    sa.Column('result_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('unit_of_measure', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('result_type_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=32), nullable=False),
    sa.Column('first_name', sa.String(length=32), nullable=False),
    sa.Column('city', sa.String(length=32), nullable=False),
    sa.Column('address', sa.String(length=64), nullable=False),
    sa.Column('zip_code', sa.String(length=32), nullable=False),
    sa.Column('phone_number', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('supervisor_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['supervisor_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('blogposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('contents', sa.Text(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('daily_schedules',
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('is_completed', sa.Boolean(), nullable=False),
    sa.Column('schedule_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('schedule_id')
    )
    op.create_table('fitboxes',
    sa.Column('serial_number', sa.String(length=128), nullable=False),
    sa.Column('qr_code', sa.String(length=128), nullable=False),
    sa.Column('model', sa.String(length=128), nullable=True),
    sa.Column('latitude', sa.Numeric(), nullable=True),
    sa.Column('longitude', sa.Numeric(), nullable=True),
    sa.Column('leftarmplate_level', sa.Integer(), nullable=True),
    sa.Column('rightarmplate_level', sa.Integer(), nullable=True),
    sa.Column('middleplate_level', sa.Integer(), nullable=True),
    sa.Column('current_user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['current_user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('serial_number'),
    sa.UniqueConstraint('qr_code')
    )
    op.create_table('medical_checks',
    sa.Column('check_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('body_weight_kg', sa.Float(), nullable=True),
    sa.Column('ibm', sa.Float(), nullable=True),
    sa.Column('valid_until_date_time', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('check_id')
    )
    op.create_table('patient_infos',
    sa.Column('patient_info_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('limitations', sa.String(length=128), nullable=True),
    sa.Column('body_length_cm', sa.Float(), nullable=True),
    sa.Column('upper_leg_length_cm', sa.Float(), nullable=True),
    sa.Column('lower_leg_length_cm', sa.Float(), nullable=True),
    sa.Column('shoe_size', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('patient_info_id')
    )
    op.create_table('exercises',
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.Column('exercise_type_id', sa.Integer(), nullable=False),
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('is_completed', sa.Boolean(), nullable=False),
    sa.Column('reps', sa.Integer(), nullable=False),
    sa.Column('series', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('rest', sa.Integer(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=False),
    sa.Column('range_of_motion', sa.Integer(), nullable=False),
    sa.Column('leftarmplate_level', sa.Integer(), nullable=False),
    sa.Column('rightarmplate_level', sa.Integer(), nullable=False),
    sa.Column('middleplate_level', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['exercise_type_id'], ['exercise_types.exercise_type_id'], ),
    sa.ForeignKeyConstraint(['schedule_id'], ['daily_schedules.schedule_id'], ),
    sa.PrimaryKeyConstraint('exercise_id')
    )
    op.create_table('trainings',
    sa.Column('training_id', sa.Integer(), nullable=False),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.Column('performed_reps', sa.Integer(), nullable=False),
    sa.Column('performed_series', sa.Integer(), nullable=False),
    sa.Column('valid_until_date_time', sa.DateTime(), nullable=True),
    sa.Column('end_date_time', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.exercise_id'], ),
    sa.PrimaryKeyConstraint('training_id')
    )
    op.create_table('results',
    sa.Column('result_id', sa.Integer(), nullable=False),
    sa.Column('result_type_id', sa.Integer(), nullable=False),
    sa.Column('training_id', sa.Integer(), nullable=False),
    sa.Column('actual_value', sa.Numeric(), nullable=False),
    sa.Column('expected_value', sa.Numeric(), nullable=True),
    sa.Column('upper_control_limit', sa.Numeric(), nullable=True),
    sa.Column('lower_control_limit', sa.Numeric(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['result_type_id'], ['result_types.result_type_id'], ),
    sa.ForeignKeyConstraint(['training_id'], ['trainings.training_id'], ),
    sa.PrimaryKeyConstraint('result_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('trainings')
    op.drop_table('exercises')
    op.drop_table('patient_infos')
    op.drop_table('medical_checks')
    op.drop_table('fitboxes')
    op.drop_table('daily_schedules')
    op.drop_table('blogposts')
    op.drop_table('users')
    op.drop_table('result_types')
    op.drop_table('exercise_types')
    # ### end Alembic commands ###
