from pydantic import AwareDatetime, BaseModel

class TransactionIn(BaseModel):
    description: str | None = None
    category: str | None = None
    date: AwareDatetime | None = None
    value: int = 0


class TransactionUpdate(BaseModel):
    description: str | None = None
    category: str | None = None
    date: AwareDatetime | None = None
    value: int = 0
