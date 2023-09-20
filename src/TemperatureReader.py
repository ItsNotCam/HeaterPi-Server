import Adafruit_DHT
import time
from datetime import datetime

def c_to_f(c):
    return (c * 9/5) + 32

def read_temperature():
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4

    h = 0
    t = 0

    while h < 1 and t < 1:
        current_time = datetime.now().strftime("%H:%M:%S")
        _,t = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if(t is not None):
            t = (t*9/5) + 32 
            print(f"{current_time} Temperature: {t}")
            break
        else:
            t = 0

    return t