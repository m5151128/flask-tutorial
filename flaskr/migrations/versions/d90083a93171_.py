"""empty message

Revision ID: d90083a93171
Revises: 050dddb4596b
Create Date: 2020-11-18 05:11:11.344496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd90083a93171'
down_revision = '050dddb4596b'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='posts', column_name='created', existing_type=sa.DateTime, new_column_name='created_at')


def downgrade():
    op.alter_column(table_name='posts', column_name='created_at', existing_type=sa.DateTime, new_column_name='created')
