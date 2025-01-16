from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from tgbot.config import DatabaseConfig


def create_engine(db: DatabaseConfig, echo: bool = False) -> AsyncEngine:
    """ Create a new async engine instance. """
    engine = create_async_engine(
        url=db.construct_sqlalchemy_url(),
        echo=echo
    )
    return engine


def create_session_pool(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    """ Create a session pool bound to the specified engine. """
    session_pool = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )
    return session_pool
