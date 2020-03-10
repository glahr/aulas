from pyfirmata2 import Arduino
from time import sleep

def my_cb(data):
    print(data)

board = Arduino(Arduino.AUTODETECT)

board.samplingOn(12)  # ms

board.analog[0].register_callback(my_cb)
board.analog[0].enable_reporting()

# board.pass_time(1)

lenPin = board.get_pin('d:11:p')

for t in range(200):
    sleep(0.050)
    lenPin.write(.8)
    #print("READ", board.analog[0].read())

#https://forum.arduino.cc/index.php?topic=70641.0

board.exit()
