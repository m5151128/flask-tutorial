"""empty message

Revision ID: 050dddb4596b
Revises: 47224eeeced1
Create Date: 2020-11-18 04:33:40.259900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '050dddb4596b'
down_revision = '47224eeeced1'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='posts', column_name='author_id', existing_type=sa.Integer, new_column_name='user_id')


def downgrade():
    op.alter_column(table_name='posts', column_name='user_id', existing_type=sa.Integer, new_column_name='author_id')
