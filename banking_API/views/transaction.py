from decimal import Decimal

from pydantic import AwareDatetime, BaseModel, computed_field

from ..models.transaction import TransactionType
from ..domain.money import Money


class TransactionOut(BaseModel):
    id: int
    account_id: int
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
