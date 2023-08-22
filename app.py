from flask import Flask, jsonify, send_file
from gpiozero import LED, Button
from picamera import PiCamera
import subprocess
import os, sys, time
import re

app = Flask(__name__)

# Cam
camera = PiCamera()

def capture():
    camera.capture('latest.jpg')

# Light
led = LED(17)
led.off()
button = Button(27)

def light_toggle():
    led.toggle()

button.when_pressed = light_toggle

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
    return jsonify({'temperature_cpu': float(output), 'temperature_1': getTemperature('28-3ce10457589d'), 'temperature_2': getTemperature('dummy'), 'light': led.is_lit})

@app.route('/light', methods=['GET'])
def get_light():
    return jsonify({'active': led.is_lit})

@app.route('/light', methods=['POST'])
def post_light():
    light_toggle()
    return '', 204

@app.route('/cam', methods=['GET'])
def get_cam():
    capture()
    return send_file('latest.jpg', mimetype='image/jpeg')

@app.route('/cam', methods=['POST'])
def post_cam():
    capture()
    return '', 204