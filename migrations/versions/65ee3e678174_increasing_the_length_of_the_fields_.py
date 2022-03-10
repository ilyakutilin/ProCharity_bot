"""increasing the length of the fields last_name and first_name up to 64

Revision ID: 65ee3e678174
Revises: 39c007beee2e
Create Date: 2022-03-10 18:16:42.005147

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '65ee3e678174'
down_revision = '39c007beee2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin_users', 'first_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=64),
               existing_nullable=True)
    op.alter_column('admin_users', 'last_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=64),
               existing_nullable=True)
    op.alter_column('external_site_users', 'first_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=64),
               existing_nullable=True)
    op.alter_column('external_site_users', 'last_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=64),
               existing_nullable=True)
    op.alter_column('statistics', 'added_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=64),
               existing_nullable=True)
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=64),
               existing_nullable=True)
    op.alter_column('users', 'date_registration',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'date_registration',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('users', 'last_name',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('users', 'first_name',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('statistics', 'added_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('external_site_users', 'last_name',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('external_site_users', 'first_name',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('admin_users', 'last_name',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('admin_users', 'first_name',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    # ### end Alembic commands ###
