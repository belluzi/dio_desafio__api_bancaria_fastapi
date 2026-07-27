from ..schemas.auth import LoginIn, CredentialsUpdate
from ..views.auth import AuthOut

async def login(credentials: LoginIn):
    pass


async def logout():
    pass


async def refresh_token():
    pass


async def update_credentials(data: CredentialsUpdate):
    pass
