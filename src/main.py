from fastapi import FastAPI
from src.router import router
from contextlib import asynccontextmanager
from src.db.db import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.drop_all(engine)
    print('Очистка базы')

    Base.metadata.create_all(engine)
    print('База готова к работе')

    yield
    print('Выключение')


app = FastAPI(
    title='TestFastAPI',
    lifespan=lifespan
)


app.include_router(router)
