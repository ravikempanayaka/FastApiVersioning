from fastapi import FastAPI

from client.router import get_routers

app = FastAPI()


for api in get_routers():
    app.include_router(api().router)
