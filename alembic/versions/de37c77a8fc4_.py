"""empty message

Revision ID: de37c77a8fc4
Revises: 71cc6dc42704
Create Date: 2024-11-02 14:25:34.576770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de37c77a8fc4'
down_revision = '71cc6dc42704'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Cars', sa.Column('type', sa.String(), nullable=False))
    op.add_column('Cars', sa.Column('model', sa.String(), nullable=False))
    op.drop_column('Cars', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Cars', sa.Column('name', sa.VARCHAR(), nullable=False))
    op.drop_column('Cars', 'model')
    op.drop_column('Cars', 'type')
    # ### end Alembic commands ###