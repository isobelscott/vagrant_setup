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

def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300
    time_in_air = muzzle_velocity * get_fall_time(tower_height)
    tower_range = time_in_air * muzzle_velocity
    
    delta_x = tower_x - target_x   # difference between tower_x and target_x
    delta_y = tower_y - target_y # difference between tower_y and target_y

    separation = math.sqrt(delta_x ** 2 + delta_y ** 2)
    # the x and y deltas form a triangle, find the hypotenuse
    if separation < tower_range:
        print("The target is closer than the tower range, what should we return?")
        return True
    else:
        print("The target is further than the tower range, what should we return?")
        return False

