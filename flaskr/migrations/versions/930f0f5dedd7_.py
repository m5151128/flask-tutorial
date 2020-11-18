"""empty message

Revision ID: 930f0f5dedd7
Revises: d90083a93171
Create Date: 2020-11-18 05:33:13.703308

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '930f0f5dedd7'
down_revision = 'd90083a93171'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=False))


def downgrade():
    op.drop_column('users', 'created_at')
