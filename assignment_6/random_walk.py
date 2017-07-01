import random
import sys

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

                # access the dictionary
                # UPDATE HERE: how do you use the key to access a dictionary?
                # replace None with the answer
        return displacements[dir_key]

def take_walk(steps):
        current_location = [0, 0]
        for step_index in range(steps):
            direction = get_random_direction()
            displacement = get_direction_displacement(direction)

        # extract the numerical values from the tuple
            delta_x = displacement[0]
            delta_y = displacement[1]

        # UPDATE current_location HERE
        # consult example in 'Storing and Updating State' for method to update
        # current_location

            current_location = [0, 0]
            current_location[0] += delta_x
            current_location[1] += delta_y

        return current_location

def take_all_walks(steps, runs):
    endpoints = []
    for walks in range(runs):
        end_location = take_walk(steps)
        endpoints.append(end_location[:], end_location[0], end_location[1])
    return endpoints


if __name__ == "__main__":
        steps = 10
        if len(sys.argv) > 1:
            steps = int(sys.argv[1])
        
        runs = 1
        if len(sys.argv) > 2:
            steps = int(sys.argv[2])

        end_locations  = take_all_walks(steps, runs)

        print("Done with all walks, printing all end locations: ")
        print(end_locations)
