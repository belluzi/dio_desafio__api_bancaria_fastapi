from fastapi import APIRouter
from ..services import account as service
from ..views.account import AccountOut


router = APIRouter(prefix="/accounts")

@router.post("/")
async def create():
    return await service.create()


@router.get("/{account_id}", response_model=AccountOut)
async def get(account_id: int):
    return await service.get(account_id)


@router.get("/me", response_model=AccountOut)
async def get_my_account(account_id: int):
    return await service.get(account_id)
