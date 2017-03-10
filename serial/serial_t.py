import serial
import binascii

t = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    s = t.read()
    if s:
        print binascii.b2a_hex(s)
