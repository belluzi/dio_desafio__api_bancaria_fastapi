import sqlalchemy as sa
from .account import accounts
from .transaction import transactions


def statement_query(account_id: int) -> sa.Select:
    return (
        sa.select(
            accounts.c.id.label("account_id"),
            accounts.c.agency,
            accounts.c.number.label("account_number"),
            accounts.c.digit.label("account_digit"),
            accounts.c.owner_name,
            accounts.c.balance_cents.label("current_balance_cents"),
            transactions.c.id.label("transaction_id"),
            transactions.c.type.label("transaction_type"),
            transactions.c.amount_cents,
            transactions.c.description,
            transactions.c.occurred_at,
            transactions.c.balance_after_cents,
        )
        .select_from(
            accounts.outerjoin(
                transactions,
                accounts.c.id == transactions.c.account_id,
            )
        )
        .where(accounts.c.id == account_id)
        .order_by(transactions.c.occurred_at.asc())
    )
