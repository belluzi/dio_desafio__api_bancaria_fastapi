from datetime import datetime, timezone
from decimal import Decimal

from pydantic import AwareDatetime, BaseModel, Field, computed_field

from ..models.transaction import TransactionType
from ..models.money import Money


class StatementTransactionOut(BaseModel):
    id: int
    type: TransactionType
    amount_cents: int
    description: str | None = None
    occurred_at: AwareDatetime | None = None
    balance_after_cents: int | None = None

    @computed_field
    @property
    def amount(self) -> Decimal:
        return Money.from_cents(self.amount_cents).to_decimal()

    @computed_field
    @property
    def balance_after(self) -> Decimal | None:
        if self.balance_after_cents is None:
            return None

        return Money.from_cents(self.balance_after_cents).to_decimal()


class StatementOut(BaseModel):
    account_id: int
    agency: str
    account_number: str
    account_digit: str | None = None
    owner_name: str
    current_balance_cents: int
    issued_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    transactions: list[StatementTransactionOut]

    @computed_field
    @property
    def current_balance(self) -> Decimal:
        return Money.from_cents(self.current_balance_cents).to_decimal()
