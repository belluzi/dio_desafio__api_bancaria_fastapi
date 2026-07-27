from decimal import Decimal
from pydantic import BaseModel, Field, field_validator
from ..models.money import Money


class AccountIn(BaseModel):
    owner_name: str = Field(min_length=3, max_length=120)
    owner_document: str = Field(min_length=11, max_length=14)
    agency: str = Field(default="0001", max_length=10)
    number: str = Field(max_length=20)
    digit: str | None = Field(default=None, max_length=2)
    initial_balance: Decimal = Field(default=Decimal("0"), ge=Decimal("0"), max_digits=12, decimal_places=2)

    @field_validator("initial_balance")
    @classmethod
    def validate_initial_balance(cls, value: Decimal) -> Decimal:
        return Money.from_decimal(value).to_decimal()

    @property
    def initial_balance_cents(self) -> int:
        return Money.from_decimal(self.initial_balance).cents
