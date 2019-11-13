from flask import Flask
import datetime
from grovepi import *

app = Flask(__name__)

LED_PIN = 3

@app.route('/')
def root():
    return 'Hello to my light'

@app.route('/lightOn')
def light_on():
    led = digitalWrite(LED_PIN,1)
    return f'Light is On'

@app.route('/lightOff')
def light_off():
    led = digitalWrite(LED_PIN,0)
    return f'Light is Off'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')
