from flask import Flask, request
from flask_socketio import SocketIO, emit
import time, threading 

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
connected = []
# Function to send text 
def send_text(text, client_sid):
    print("sending:", text)
    #emit('incoming_text', text, namespace="/")
    socketio.emit('incoming_text', text, namespace='/', room=client_sid)


@socketio.on('connect', namespace="/") 
def handle_connect():
    print('Client connected:', request.sid)
    connected.append(request.sid)
    #global client_sid
    #client_sid = request.sid
    # Start test function as background task
    #socketio.start_background_task(test)
    
def test():
    while(len(connected)==0):
        time.sleep(1)
    print("starting")
    

    lines = ["Line 1", "Line 2", "Line 3"]
    c = 0
    while True:
        c+=1
        line = lines[c%len(lines)]
        #socketio.sleep(0.5) 
        time.sleep(1)
        send_text(line, connected[0])

    print("done")

if __name__ == '__main__':
    t = threading.Thread(target=test)
    t.daemon = True
    t.start()
    socketio.run(app, )