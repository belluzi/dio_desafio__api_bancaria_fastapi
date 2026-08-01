from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from .money import Money

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


@dataclass(frozen=True)
class Transaction:

    id: int | None
    account_id: int
    type: TransactionType
    amount: Money
    description: str | None
    occurred_at: datetime
    balance_after: Money
    created_at: datetime | None


    @property
    def is_deposit(self) -> bool:

        return self.type is TransactionType.DEPOSIT


    @property
    def is_withdraw(self) -> bool:

        return self.type is TransactionType.WITHDRAW


    @property
    def has_description(self) -> bool:

        return bool(self.description and self.description.strip())


    @classmethod
    def deposit(cls, account_id: int, amount: Money, balance_after: Money, description: str | None, occurred_at: datetime) -> Transaction:

        return cls._create(account_id, TransactionType.DEPOSIT, amount, balance_after, description, occurred_at)


    @classmethod
    def withdraw(cls, account_id: int, amount: Money, balance_after: Money, description: str | None, occurred_at: datetime) -> Transaction:

        return cls._create(account_id, TransactionType.WITHDRAW, amount, balance_after, description, occurred_at)


    @classmethod
    def _create(cls, account_id: int, transaction_type: TransactionType, amount: Money, balance_after: Money, description: str | None, occurred_at: datetime) -> Transaction:

        return cls(
            id=None,
            account_id=account_id,
            type=transaction_type,
            amount=amount,
            description=description.strip() if description else None,
            occurred_at=occurred_at,
            balance_after=balance_after,
            created_at=None
        )
