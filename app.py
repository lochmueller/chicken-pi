from flask import Flask, jsonify, send_file, request
from gpiozero import LED, Button
from picamera import PiCamera
import subprocess
import os, sys
import re

app = Flask(__name__)

# Configuration
pinLed = 17
pinLedButton = 27
pinThermData = 4

# Cam
camera = PiCamera()

def capture():
    camera.capture('latest.jpg')

# Light
led = LED(pinLed)
led.off()
button = Button(pinLedButton)

def light_toggle():
    led.toggle()

button.when_pressed = light_toggle

# Door
doorState = 'open'
def door_toggle():
    if doorState == 'open':
        door_closed()
    else:
        door_open()
def door_open():
    # Handle door here
    doorState = 'open'
    return False
def door_closed():
    # Handle door here
    doorState = 'closed'
    return False

# Temperature
def getTemperature(device: str) -> float:
    filePath = "/sys/bus/w1/devices/"+device+"/w1_slave"
    if os.path.isfile(filePath) == False:
        return 0.0
    file = open(filePath)
    filecontent = file.read()
    file.close()
    return float(re.search('t=(\d*)', filecontent).group(1)) / 1000

###
### REST API
###
@app.route('/info', methods=['GET'])
def get_info():
    output = subprocess.check_output("vcgencmd measure_temp | grep  -o -E '[[:digit:].]*'", shell=True)
    result = {
        'temperature_cpu': float(output),
        'temperature_1': getTemperature('28-3ce10457589d'),
        'temperature_2': getTemperature('28-3ce10457601d'),
        'light': 'on' if led.is_lit else 'off',
        'door': doorState
    }
    return jsonify(result)

@app.route('/light', methods=['POST'])
def post_light():
    newState = request.args.get('state', 'toggle')
    if newState == 'on':
        led.on()
    elif newState == 'off':
        led.off()
    else:
        light_toggle()
    return '', 204

@app.route('/door', methods=['POST'])
def post_door():
    newState = request.args.get('state', 'toggle')
    if newState == 'open':
        door_open()
    elif newState == 'closed':
        door_closed()
    else:
        door_toggle()
    return '', 204

@app.route('/cam', methods=['GET'])
def get_cam():
    capture()
    return send_file('latest.jpg', mimetype='image/jpeg')
