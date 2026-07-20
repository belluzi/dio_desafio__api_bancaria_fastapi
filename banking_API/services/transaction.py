from ..schemas.transaction import TransactionIn, TransactionUpdate


async def create(transaction: TransactionIn):
    pass


async def read_all():
    pass


async def update(transaction_id: int, data: TransactionUpdate):
    pass


async def delete(transaction_id: int):
    pass
