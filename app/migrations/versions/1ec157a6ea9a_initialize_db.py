"""initialize db

Revision ID: 1ec157a6ea9a
Revises: 
Create Date: 2024-03-05 01:08:45.842124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ec157a6ea9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class',
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('course_title', sa.String(), nullable=True),
    sa.Column('course_status', sa.String(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.teacher_id'], ),
    sa.PrimaryKeyConstraint('class_id')
    )
    op.create_table('student',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('student_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.teacher_id'], ),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('teachers',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('teacher_name', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['class.class_id'], ),
    sa.PrimaryKeyConstraint('teacher_id')
    )
    op.create_table('fee',
    sa.Column('fee_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('fee_status', sa.String(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['class.class_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('fee_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fee')
    op.drop_table('teachers')
    op.drop_table('student')
    op.drop_table('class')
    # ### end Alembic commands ###
