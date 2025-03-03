from fastapi import FastAPI
from routers import items, users, socket, getdday
from sockets import sio_app
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins={
    "https://snsapp.pages.dev"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(socket.router)
app.include_router(getdday.router)

app.mount('/ws', app=sio_app)

@app.get("/")
def read_root():
    return {"Hello": "World"}


