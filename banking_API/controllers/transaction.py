from fastapi import APIRouter, Response, status
from ..schemas.transaction import TransactionIn, TransactionUpdate
from ..services import transaction as service
from ..views.transaction import TransactionOut

router = APIRouter(prefix="/transactions")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create(transaction: TransactionIn):
    return await service.create(transaction)


@router.get("/", response_model=list[TransactionOut])
async def read_transactions():
    return await service.read_all()


@router.patch("/{transaction_id}", status_code=status.HTTP_200_OK, response_model=TransactionOut)
async def update(transaction_id: int, data: TransactionUpdate):
    return await service.update(transaction_id, data)


@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(transaction_id: int):
    await service.delete(transaction_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)