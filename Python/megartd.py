from machine import I2C
from machine import Pin
import struct

MEGARTD_ADDRESS = 0x40
MEGARTD_TEMPERATURE_ADD = 0

def get(stack, channel):
    i2c = I2C(scl=Pin(22), sda=Pin(21),freq=400000)
    val = []
    if stack < 0 or stack > 7:
        raise ValueError('Invalid stack level')
        return
    
    if channel < 1 or channel > 8:
        raise ValueError('Invalid channel number')
        return
    
    buff = i2c.readfrom_mem(MEGARTD_ADDRESS+stack, MEGARTD_TEMPERATURE_ADD + (4 * (channel - 1)), 4)
    val = struct.unpack('f', bytearray(buff))

    return val[0]  