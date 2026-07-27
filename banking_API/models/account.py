import sqlalchemy as sa
from ..db import metadata


accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("agency", sa.String(10), nullable=False, server_default="0001"),
    sa.Column("number", sa.String(20), nullable=False),
    sa.Column("digit", sa.String(2), nullable=True),
    sa.Column("owner_name", sa.String(120), nullable=False),
    sa.Column("owner_document", sa.String(14), nullable=False),
    sa.Column("balance_cents", sa.Integer, nullable=False, server_default="0"),
    sa.Column("is_active", sa.Boolean, nullable=False, server_default=sa.text("1")),
    sa.Column(
        "created_at",
        sa.TIMESTAMP(timezone=True),
        nullable=False,
        server_default=sa.func.now(),
    ),
    sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=True),
    sa.UniqueConstraint("agency", "number", "digit", name="uq_accounts_agency_number_digit"),
    sa.CheckConstraint("balance_cents >= 0", name="ck_accounts_balance_cents_non_negative"),
)
