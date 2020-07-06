import smbus
import time

bus = smbus.SMBus(0)

address = 0x40

def writeNumber(value):
    bus.write_byte(address,value)
    return -1

while True:
    var = int(input())

    if not var:
        continue

    writeNumber(var)
