"""empty message

Revision ID: c05f8fe3793c
Revises: 0dd93afc1c34
Create Date: 2020-03-16 15:41:20.228078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c05f8fe3793c'
down_revision = '0dd93afc1c34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('PAN',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('docid', sa.String(length=16), nullable=True),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_PAN_docid'), 'PAN', ['docid'], unique=True)
    op.create_index(op.f('ix_PAN_firstname'), 'PAN', ['firstname'], unique=False)
    op.create_index(op.f('ix_PAN_lastname'), 'PAN', ['lastname'], unique=False)
    op.create_table('aadhar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('docid', sa.String(length=16), nullable=True),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_aadhar_docid'), 'aadhar', ['docid'], unique=True)
    op.create_index(op.f('ix_aadhar_firstname'), 'aadhar', ['firstname'], unique=False)
    op.create_index(op.f('ix_aadhar_lastname'), 'aadhar', ['lastname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_aadhar_lastname'), table_name='aadhar')
    op.drop_index(op.f('ix_aadhar_firstname'), table_name='aadhar')
    op.drop_index(op.f('ix_aadhar_docid'), table_name='aadhar')
    op.drop_table('aadhar')
    op.drop_index(op.f('ix_PAN_lastname'), table_name='PAN')
    op.drop_index(op.f('ix_PAN_firstname'), table_name='PAN')
    op.drop_index(op.f('ix_PAN_docid'), table_name='PAN')
    op.drop_table('PAN')
    # ### end Alembic commands ###
