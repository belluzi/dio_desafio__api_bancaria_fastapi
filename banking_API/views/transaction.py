from pydantic import AwareDatetime, BaseModel

class TransactionOut(BaseModel):
    id: int
    description: str
    category: str
    date: AwareDatetime | None
    value: int = 0