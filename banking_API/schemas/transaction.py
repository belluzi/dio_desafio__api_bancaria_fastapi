from decimal import Decimal

from pydantic import AwareDatetime, BaseModel, Field, field_validator

from ..models.transaction import TransactionType
from ..domain.money import Money


class TransactionIn(BaseModel):
    account_id: int
    type: TransactionType
    amount: Decimal = Field(gt=Decimal("0"), max_digits=12, decimal_places=2)
    description: str | None = None
    occurred_at: AwareDatetime | None = None

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: Decimal) -> Decimal:
        return Money.from_decimal(value).ensure_positive().to_decimal()

    @property
    def amount_cents(self) -> int:
        return Money.from_decimal(self.amount).ensure_positive().cents


class TransactionUpdate(BaseModel):
    type: TransactionType | None = None
    amount: Decimal | None = Field(default=None, gt=Decimal("0"), max_digits=12, decimal_places=2)
    description: str | None = None
    occurred_at: AwareDatetime | None = None

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: Decimal | None) -> Decimal | None:
        if value is None:
            return None

        return Money.from_decimal(value).ensure_positive().to_decimal()

    @property
    def amount_cents(self) -> int | None:
        if self.amount is None:
            return None

        return Money.from_decimal(self.amount).ensure_positive().cents
