import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import AsyncIterator
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = BASE_DIR / "banking_api.db"
DEFAULT_DATABASE_URL = f"sqlite+aiosqlite:///{DEFAULT_DB_PATH.as_posix()}"


def resolve_database_url() -> str:
    raw_database_url = os.getenv("DATABASE_URL")

    if not raw_database_url:
        return DEFAULT_DATABASE_URL

    if raw_database_url.startswith("sqlite:///"):
        return raw_database_url.replace("sqlite:///", "sqlite+aiosqlite:///")

    return raw_database_url


DATABASE_URL = resolve_database_url()
metadata = sa.MetaData()
engine_options = {}

if DATABASE_URL.startswith("sqlite"):
    engine_options["connect_args"] = {
        "check_same_thread": False
    }

engine: AsyncEngine = create_async_engine(DATABASE_URL, **engine_options)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

@asynccontextmanager
async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session

from . import models as _models  # noqa: E402,F401
