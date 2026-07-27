from pydantic import BaseModel

class AuthOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
