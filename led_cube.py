from machine import Pin
import utime


class LedCube:

    def __init__(self, level_pins, led_pins):
        if not len(level_pins) % len(led_pins) == 0:
            raise CubeException("led_pins array length does not divide with level_pins array length. len(level_pins) = ", len(level_pins), ", len(led_pins) = ", len(led_pins))
        self.level_pins = map(lambda p: Pin(p, Pin.OUT), level_pins)
        self.led_pins = map(lambda p: Pin(p, Pin.OUT), led_pins)

    
    
    

class CubeException(Exception):
    def __init__(self, message):
        self.message = message