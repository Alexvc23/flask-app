"""Update Affaire model to enforce uniqueness, Unique Affaire per user

Revision ID: e1b724d1b114
Revises: 471f3b428f0f
Create Date: 2024-04-23 10:41:05.774717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1b724d1b114'
down_revision = '471f3b428f0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('affaire', schema=None) as batch_op:
        batch_op.create_unique_constraint('uix_nom_user_id', ['nom', 'user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('affaire', schema=None) as batch_op:
        batch_op.drop_constraint('uix_nom_user_id', type_='unique')

    # ### end Alembic commands ###
