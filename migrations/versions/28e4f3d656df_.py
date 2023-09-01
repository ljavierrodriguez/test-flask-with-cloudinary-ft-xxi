"""empty message

Revision ID: 28e4f3d656df
Revises: dd1e0ae593d7
Create Date: 2023-09-01 10:58:14.881804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28e4f3d656df'
down_revision = 'dd1e0ae593d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=120), nullable=False),
    sa.Column('media', sa.String(length=20), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('portfolios_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['portfolios_id'], ['portfolios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photos')
    op.drop_table('portfolios')
    # ### end Alembic commands ###
