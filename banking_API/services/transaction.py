import sqlalchemy as sa
from fastapi import HTTPException, status

from ..db import get_session
from ..models.account import accounts
from ..domain.money import Money
from ..models.transaction import TransactionType, transactions
from ..schemas.transaction import TransactionIn, TransactionUpdate
from ..views.transaction import TransactionOut


async def create(transaction: TransactionIn) -> TransactionOut:
    amount = Money.from_cents(transaction.amount_cents).ensure_positive()

    async with get_session() as session:
        async with session.begin():
            account_result = await session.execute(sa.select(accounts).where(accounts.c.id == transaction.account_id).with_for_update())
            account = account_result.mappings().one_or_none()

            if account is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada")

            if not account["is_active"]:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Conta inativa")

            current_balance = Money.from_cents(account["balance_cents"])

            if transaction.type == TransactionType.DEPOSIT:
                new_balance = current_balance.add(amount)

            if transaction.type == TransactionType.WITHDRAW:
                new_balance = current_balance.subtract(amount)

            insert_values = {
                "account_id": transaction.account_id,
                "type": transaction.type.value,
                "amount_cents": amount.cents,
                "description": transaction.description,
                "balance_after_cents": new_balance.cents,
            }

            if transaction.occurred_at is not None:
                insert_values["occurred_at"] = transaction.occurred_at

            stmt = (sa.insert(transactions).values(**insert_values).returning(transactions))

            result = await session.execute(stmt)

            await session.execute(sa.update(accounts).where(accounts.c.id == account["id"]).values(balance_cents=new_balance.cents))

            created_transaction = result.mappings().one()

    return TransactionOut.model_validate(created_transaction)


async def read_all():
    pass


async def update(transaction_id: int, data: TransactionUpdate):
    pass


async def delete(transaction_id: int):
    pass
