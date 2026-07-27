from decimal import Decimal
from pydantic import AwareDatetime, BaseModel, computed_field
from ..models.money import Money


class AccountOut(BaseModel):
    id: int
    agency: str
    number: str
    digit: str | None = None
    owner_name: str
    balance_cents: int
    is_active: bool
    created_at: AwareDatetime | None = None
    updated_at: AwareDatetime | None = None

    @computed_field
    @property
    def balance(self) -> Decimal:
        return Money.from_cents(self.balance_cents).to_decimal()
