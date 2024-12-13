from fastapi import FastAPI
from routers import items, users, socket
from sockets import sio_app

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
app.include_router(socket.router)

app.mount('/ws', app=sio_app)

@app.get("/")
def read_root():
    return {"Hello": "World"}


