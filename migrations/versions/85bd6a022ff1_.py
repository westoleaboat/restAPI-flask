"""empty message

Revision ID: 85bd6a022ff1
Revises: bce08bf52f40
Create Date: 2022-12-03 11:39:30.372358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85bd6a022ff1'
down_revision = 'bce08bf52f40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # with op.batch_alter_table('items', schema=None) as batch_op:
    #     batch_op.add_column(sa.Column('description', sa.String(), nullable=True))
    pass

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
