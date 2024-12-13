import socketio

sio_client = socketio.Client(reconnection=True,
                             reconnection_attempts=0)

@sio_client.event
def connect():
    print('I\'m connected')

@sio_client.event
def disconnect():
    print('I\'m disconnected')

@sio_client.event
def message(data):
    print(data)

sio_client.connect('http://localhost:8000/ws',
                   socketio_path='/ws/socket.io')
sio_client.wait()