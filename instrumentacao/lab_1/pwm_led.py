from pyfirmata2 import Arduino
from time import sleep
import matplotlib.pyplot as plt

signal = []

def my_cb(data):
    # print(data)
    signal.append(data)
    #pass

board = Arduino(Arduino.AUTODETECT)

board.samplingOn(10)  # ms

board.analog[0].register_callback(my_cb)
board.analog[0].enable_reporting()

lenPin = board.get_pin('d:3:p')

lum = 0
delta_lum = 0.05;

for t in range(50):
    sleep(0.5)
    if lum > 1.0 or lum < 0:
        delta_lum = -delta_lum
    lum += delta_lum
    lenPin.write(lum)

lenPin.write(0)

plt.plot(signal)
plt.show()

board.exit()
