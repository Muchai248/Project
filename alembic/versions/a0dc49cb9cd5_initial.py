"""initial

Revision ID: a0dc49cb9cd5
Revises: 
Create Date: 2023-09-07 21:20:30.004879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0dc49cb9cd5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tenants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=255), nullable=False),
        sa.Column('last_name', sa.String(length=255), nullable=False),
        sa.Column('house_id', sa.Integer(),sa.ForeignKey("houses.id"), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'houses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('house_number', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        'caretakers',
        sa.Column('id', sa.Integer),
        sa.Column("owner_name",sa.String()),
        sa.Column('house_id', sa.Integer(),sa.ForeignKey("houses.id"), nullable=False),
        # sa.Column('tenant_id', sa.Integer(),sa.ForeignKey("tenants.id"), nullable=False),
        sa.PrimaryKeyConstraint("id")
        
    )
    


def downgrade() -> None:
    op.drop_table('caretakers')
    op.drop_table('houses')
    op.drop_table('tenants')
