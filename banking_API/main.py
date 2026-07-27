from contextlib import asynccontextmanager
from fastapi import FastAPI
from .controllers.statement import router as statement_router
from .controllers.transaction import router as transaction_router
from .controllers.account import router as account_router
from .controllers.auth import router as auth_router
from .db import engine, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    try:
        yield
    finally:
        await engine.dispose()


app = FastAPI(lifespan=lifespan)


app.include_router(transaction_router)
app.include_router(statement_router)
app.include_router(account_router)
app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"message": "API Bancaria Assincrona com FastAPI"}
