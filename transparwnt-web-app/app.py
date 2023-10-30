from flask import Flask, render_template, request
from flask_socketio import SocketIO
import time
import threading
import random
import requests
#from xo.redis import xoRedis

#xo = xoRedis("flame",port=6679)

app = Flask(__name__)
#socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow connections from all origins

@socketio.on('connect', namespace='/')
def handle_connect():
    print('Client connected:', request.sid)

@socketio.on('disconnect', namespace='/')
def handle_disconnect():
    print('Client disconnected:', request.sid)

@app.route('/')
def index():
    return render_template('your_webpage.html')
hue_cycling = True  # Initial state for hue cycling
hue_speed = 1.0     # Initial hue cycle speed

def get_cursor_coordinates_and_values():
    global hue_cycling, hue_speed

    c = 0
    ring_size = 100
    while True:
        c += 1
        cursor_x = random.randint(0, 1400)
        cursor_y = random.randint(0, 800)
        hue = random.randint(0, 180)
        ring_size = 100 + random.randint(0, 300)
        blur_value = random.uniform(0.1, 5.0)

        #if hue_cycling:
        #    hue_speed = max(0.1, min(10.0, hue_speed))  # Ensure hue_speed is in the range [0.1, 10.0]
        #    # hue_rotation = (time.time() * hue_speed) % 360.0
        #    pass
        #else:
        #    hue_rotation = hue  # If not cycling, use a fixed hue value (e.g., 0 degrees)
        #print("#######################################################")
        playWithSize = True
        if playWithSize:
            move = False
            if move:
                socketio.emit('cursorCoordinates', {'x': cursor_x, 'y': cursor_y}, namespace='/')

            socketio.emit('ringSize', (ring_size*0.8, not move), namespace='/')
            #socketio.emit('blurValue', blur_value, namespace='/')
            #socketio.emit('hueControl', {'cycling': hue_cycling, 'speed': hue_speed, 'rotation': hue_rotation}, namespace='/')
        #print("#######################################################")
        nl = '\n'
        xText = f"{c}{str(nl if c%5 == 0 else '')}"
        socketio.emit("changeText",(xText),namespace='/')
        print(f"########################{xText}###############################")
        time.sleep(1)

def prepWindow(v="Hello Flame", *args, **kwargs):
    socketio.emit("prepWindow",(),namespace='/')
    print("Prepping window",v)
    
    
def sendText(v="Hello Flame", *args, **kwargs):
    socketio.emit("changeText",(v),namespace='/')
    print("Sending Text to UI",v)

def clearText(v=None, *args, **kwargs):
    socketio.emit("clearText",(),namespace='/')
    print("Clearing Text on UI")

def makeSmall(v=0, *args, **kwargs):
    socketio.emit('ringSize', (150+v, True), namespace='/')
    print("Going Small")

def makeSize(v=0, *args, **kwargs):
    socketio.emit('ringSize', (v, True), namespace='/')
    print(f"Going Size:{v}")
    
def makeBig(v=0, *args, **kwargs):
    socketio.emit('ringSize', (300+v, True), namespace='/')
    print("Going Big")
    

def setDirectionRTL(v=0, *args, **kwargs):
    socketio.emit('setDirectionRTL', namespace='/')
    print("RTL")

def setDirectionLTR(v=0, *args, **kwargs):
    socketio.emit('setDirectionLTR', namespace='/')
    print("LTR")
    
    
    

#xo.small @= makeSmall
#xo.big @= makeBig

# @socketio.on('setHue', namespace='/')
# def set_hue(data):
#     socketio.emit('hueControl', {'rotation': data['hue']}, namespace='/')

if __name__ == '__main__':
    # Start the cursor coordinates and values sending thread
    coordinates_thread = threading.Thread(target=get_cursor_coordinates_and_values)
    coordinates_thread.daemon = True
    coordinates_thread.start()

    # Start the Flask-SocketIO server
    socketio.run(app, debug=True)
else:
    pass
    
def start(done):
    try:
        #coordinates_thread = threading.Thread(target=get_cursor_coordinates_and_values)
        #coordinates_thread.daemon = True
        #coordinates_thread.start()
        socketio.run(app)
    except:
        done[0] = True

