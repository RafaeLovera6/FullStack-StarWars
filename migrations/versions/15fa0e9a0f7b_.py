"""empty message

Revision ID: 15fa0e9a0f7b
Revises: a1dac210c905
Create Date: 2022-02-05 02:46:04.355823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15fa0e9a0f7b'
down_revision = 'a1dac210c905'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('height', sa.String(length=120), nullable=False),
    sa.Column('hair_color', sa.String(length=120), nullable=False),
    sa.Column('eye_color', sa.String(length=120), nullable=False),
    sa.Column('birth_year', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=120), nullable=False),
    sa.Column('img_url', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=120), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('img_url', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###