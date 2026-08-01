import sqlalchemy as sa
from ..db import metadata


users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("account_id", sa.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False, unique=True),
    sa.Column("username", sa.String(50), nullable=False,unique=True),
    sa.Column("email", sa.String(255), nullable=False, unique=True),
    sa.Column("password_hash", sa.String(255),nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()),
    sa.Column("last_login_at", sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column("updated_at", sa.TIMESTAMP(timezone=True),nullable=True),
    sa.Column("password_changed_at", sa.TIMESTAMP(timezone=True),nullable=True)
)
