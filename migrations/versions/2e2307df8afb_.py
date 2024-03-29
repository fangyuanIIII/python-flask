"""empty message

Revision ID: 2e2307df8afb
Revises: 
Create Date: 2024-01-01 14:26:31.287115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e2307df8afb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collects',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'movie_id')
    )
    op.drop_table('man')
    op.drop_table('person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name='sys_c007582'),
    oracle_resolve_synonyms=False
    )
    op.create_table('man',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('gradeid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['gradeid'], ['person.id'], name='sys_c007585'),
    sa.PrimaryKeyConstraint('id', name='sys_c007584')
    )
    op.drop_table('collects')
    op.drop_table('user')
    op.drop_table('movie')
    # ### end Alembic commands ###
