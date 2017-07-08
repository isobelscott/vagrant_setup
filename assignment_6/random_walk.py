#!/usr/bin/env python3

import random
import sys
import math

def get_random_direction():
        direction = ""
        probability = random.random()

        if probability < 0.25:
            direction = "west"
        elif probability < 0.5:
            direction = "east"
        elif probability < 0.75: 
            direction = "north"
        else: 
            direction = "south"

        return direction

def get_direction_displacement(dir_key):
        displacements = {
                'west': (-1, 0),
                'east': (1, 0),
                'north': (0, 1),
                'south': (0, -1)
                }

        return displacements[dir_key]

def take_walk(steps):
        current_location = [0, 0]
        
        for step_index in range(steps):
            direction = get_random_direction()
            displacement = get_direction_displacement(direction)

            delta_x = displacement[0]
            delta_y = displacement[1]

            current_location = [0, 0]
            current_location[0] += delta_x
            current_location[1] += delta_y

        return current_location

def take_all_walks(steps):
    endpoints = []
    for walks in range(steps):
        end_location = take_walk(steps)
        endpoints.append(end_location)
    return endpoints


def average_final_distance(endpoints):
    total_distance = 0
    for coords in endpoints:
        dx = coords[0]
        dy = coords[1]

        # use the Pythagorean theorem to get distance like last session
        distance = math.sqrt( dx ** 2 + dy ** 2)

        total_distance += distance

    return total_distance / len(endpoints)

# def average_position(endpoints):
    

if __name__ == "__main__":
    steps = 10
    if len(sys.argv) > 1:
    steps = int(sys.argv[1])
        
    runs = 10
    if len(sys.argv) > 2:
    steps = int(sys.argv[2])

    end_locations  = take_all_walks(runs)
    average_displacement = average_final_distance(end_locations)
        
    print("Done with all walks, printing all end locations: ")
    print(end_locations)
    print("The average distance covered on these walks is: ")
    print(average_displacement)
