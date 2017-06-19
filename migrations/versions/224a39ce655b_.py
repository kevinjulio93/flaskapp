"""empty message

Revision ID: 224a39ce655b
Revises: 
Create Date: 2017-06-18 21:50:41.220122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '224a39ce655b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('favcolor', sa.String(length=255), nullable=True),
    sa.Column('pet', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
