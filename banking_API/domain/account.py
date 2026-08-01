from dataclasses import dataclass
from datetime import datetime
from .money import Money
from .exceptions.account import InsufficientFundsError, InactiveAccountError

@dataclass
class Account:
    id: int
    agency: str
    number: str
    digit: str | None
    owner_name: str
    owner_document: str
    balance: Money
    is_active: bool
    created_at: datetime
    updated_at: datetime | None


    def deposit(self, amount: Money) -> None:

        self.ensure_active()
        amount.ensure_positive()
        self.balance = self.balance.add(amount)


    def withdraw(self, amount: Money) -> None:

        self.ensure_active()
        amount.ensure_positive()

        if amount.cents > self.balance.cents:
            raise InsufficientFundsError()

        self.balance = self.balance.subtract(amount)


    def activate(self) -> None:

        self.is_active = True


    def deactivate(self) -> None:

        self.is_active = False


    def ensure_active(self) -> None:

        if not self.is_active:
            raise InactiveAccountError()
