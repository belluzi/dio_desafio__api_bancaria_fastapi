from fastapi import APIRouter
from ..schemas.auth import CredentialsUpdate, LoginIn
from ..services import auth as service
from ..views.auth import AuthOut


router = APIRouter(prefix="/auth")


@router.post("/", response_model=AuthOut)
async def login(data: LoginIn):
    return await service.login(credentials = data)


@router.post("/logout", response_model=AuthOut)
async def logout():
    return await service.logout()


@router.post("/refresh", response_model=AuthOut)
async def refresh_token():
    return await service.refresh_token()


@router.put("/credentials", response_model=AuthOut)
async def update_credentials(data: CredentialsUpdate):
    return await service.update_credentials(data = data)
