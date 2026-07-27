from fastapi import APIRouter
from ..services import statement as service
from ..views.statement import StatementOut


router = APIRouter(prefix="/statements")


@router.get("/{account_id}", response_model=StatementOut)
async def get(account_id: int):
    return await service.get(account_id)
