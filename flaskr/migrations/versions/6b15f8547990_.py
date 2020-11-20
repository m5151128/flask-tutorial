"""empty message

Revision ID: 6b15f8547990
Revises: bc70d70f45d1
Create Date: 2020-11-20 02:20:29.444922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b15f8547990'
down_revision = 'bc70d70f45d1'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE posts RENAME INDEX author_id to user_id")


def downgrade():
    op.execute("ALTER TABLE posts RENAME INDEX user_id to author_id")
