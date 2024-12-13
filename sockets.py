import socketio

sio_server = socketio.AsyncServer(
    async_mode = 'asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='/ws/socket.io'
)

sidList = list()

@sio_server.on('connect')
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    sidList.append(sid)

@sio_server.on('disconnect')
async def disconnect(sid):
    print(f'{sid}: disconnected')
    sidList.remove(sid)

