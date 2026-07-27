from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

CENT_SCALE = Decimal("100")
TWO_DECIMAL_PLACES = Decimal("0.01")

@dataclass(frozen=True)
class Money:
    cents: int

    def __post_init__(self) -> None:
        if not isinstance(self.cents, int):
            raise TypeError("Money cents must be an integer")
        if self.cents < 0:
            raise ValueError("Money cannot be negative")

    @classmethod
    def from_decimal(cls, value: Decimal | int | str) -> "Money":
        decimal_value = cls._to_decimal(value)
        cls._validate_scale(decimal_value)
        return cls(int(decimal_value * CENT_SCALE))

    @classmethod
    def from_cents(cls, cents: int) -> "Money":
        return cls(cents)

    @classmethod
    def zero(cls) -> "Money":
        return cls(0)

    @property
    def is_zero(self) -> bool:
        return self.cents == 0

    def ensure_positive(self) -> "Money":
        if self.is_zero:
            raise ValueError("Money must be greater than zero")
        return self

    def add(self, other: "Money") -> "Money":
        return Money(self.cents + other.cents)

    def subtract(self, other: "Money") -> "Money":
        if other.cents > self.cents:
            raise ValueError("Insufficient funds")
        return Money(self.cents - other.cents)

    def to_decimal(self) -> Decimal:
        return (Decimal(self.cents) / CENT_SCALE).quantize(TWO_DECIMAL_PLACES)

    @staticmethod
    def _to_decimal(value: Decimal | int | str) -> Decimal:
        try:
            decimal_value = Decimal(str(value))
        except (InvalidOperation, ValueError) as exc:
            raise ValueError("Money value must be numeric") from exc

        if not decimal_value.is_finite():
            raise ValueError("Money value must be finite")

        if decimal_value < 0:
            raise ValueError("Money cannot be negative")

        return decimal_value

    @staticmethod
    def _validate_scale(value: Decimal) -> None:
        if value != value.quantize(TWO_DECIMAL_PLACES):
            raise ValueError("Money must have at most two decimal places")
