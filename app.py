from flask import Flask, jsonify, send_file
from gpiozero import LED, Button
from picamera import PiCamera
import subprocess

app = Flask(__name__)

# Cam
camera = PiCamera()


# @todo os.path.realpath
# @todo temperature

def capture():
    camera.capture('latest.jpg')

# Light
led = LED(4)
led.off()
button = Button(2)

def light_toggle():
    led.toggle()

button.when_pressed = light_toggle


###
### REST API
###
@app.route('/info', methods=['GET'])
def get_info():
    output = subprocess.check_output("vcgencmd measure_temp | grep  -o -E '[[:digit:].]*'", shell=True)
    return jsonify({'temperature': float(output)})

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
    return send_file('pictures/latest.jpg', mimetype='image/jpeg')

@app.route('/cam', methods=['POST'])
def post_cam():
    capture()
    return '', 204

@app.route('/temperature', methods=['GET'])
def get_temperature():
    return jsonify({'in': 0.0, 'out': 0.0})