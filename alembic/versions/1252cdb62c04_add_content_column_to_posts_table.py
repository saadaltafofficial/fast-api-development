"""Add content column to posts table

Revision ID: 1252cdb62c04
Revises: b5f948679208
Create Date: 2025-06-24 13:52:45.958314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1252cdb62c04'
down_revision: Union[str, Sequence[str], None] = 'b5f948679208'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
