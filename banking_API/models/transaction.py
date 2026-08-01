from enum import Enum
import sqlalchemy as sa
from ..db import metadata


transactions = sa.Table(
    "transactions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("account_id", sa.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False),
    sa.Column("type", sa.String(20), nullable=False),
    sa.Column("amount_cents", sa.Integer, nullable=False),
    sa.Column("description", sa.String(255), nullable=True),
    sa.Column("occurred_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()),
    sa.Column("balance_after_cents", sa.Integer, nullable=True),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()),

    sa.CheckConstraint("amount_cents > 0", name="ck_transactions_amount_cents_positive"),
    sa.CheckConstraint("type in ('deposit', 'withdraw')", name="ck_transactions_type_allowed")
)
