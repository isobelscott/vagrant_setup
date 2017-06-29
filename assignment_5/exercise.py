def to_fahrenheit(degrees_celsius):
    degrees_celsius = degrees_celsius * 1.8 + 32
    return degrees_celsius

def to_celsius(degrees_fahrenheit):
    degrees_fahrenheit = (degrees_fahrenheit - 32) / 1.8
    return degrees_fahrenheit

import math
def get_fall_time(height):
    time_elapsed = math.sqrt((2 * height) / 9.8)
    return time_elapsed

