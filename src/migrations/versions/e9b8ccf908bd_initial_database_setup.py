"""Initial database setup

Revision ID: e9b8ccf908bd
Revises: 0589425f3de6
Create Date: 2025-06-07 11:46:16.205612

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = 'e9b8ccf908bd'
down_revision: str | None = '0589425f3de6'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
