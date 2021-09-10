"""add column archive to ReasonCanceling table

Revision ID: e3e436365011
Revises: 0ea530c95a28
Create Date: 2021-09-10 22:05:49.403355

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e3e436365011'
down_revision = '0ea530c95a28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reasons_canceling', sa.Column('archive', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reasons_canceling', 'archive')
    # ### end Alembic commands ###
