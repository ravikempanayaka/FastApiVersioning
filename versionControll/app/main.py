from fastapi import FastAPI

from client.router import get_routers

app = FastAPI()


for api in get_routers():
    app.include_router(api().router)


@app.get('/hello')
# @version(1, 0)
def index():
    return 'Hello World!'

# app = VersionedFastAPI(app, enable_latest=True)
