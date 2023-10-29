import numpy as np
from itertools import product


def axis_movement(start, end, interval, max_dist):
    moves = [end - start]
    
    for lap in range(1, max_dist//interval+2):
        laps = lap * interval
        if lap % 2 == 0:
            move = laps + (end - start)
            opposite_move = -laps - (start - end)
        else:
            move = laps - (end + start) + interval
            opposite_move = -laps - (end + start) + interval

        moves.extend([move, opposite_move])
    
    return moves


def generate_directions(dX, dY, max_dist, exclusions=None):
    directions = {}
    
    for dx, dy in list(product(dX, dY)):
        if dx == dy == 0:
            continue
        
        dist = (dx**2 + dy**2) ** 0.5
        if dist > max_dist:
            continue
        
        gcd = abs(np.gcd(dx, dy))
        d = (dx//gcd, dy//gcd)
        
        if exclusions and d in exclusions and exclusions[d] < dist:
            continue
        if d in directions and directions[d] < dist:
            continue
        
        directions[d] = dist
    
    return directions


def solution(dimensions, your_position, trainer_position, distance):
    w, h = dimensions
    x_start, y_start = your_position
    x_end, y_end = trainer_position

    dX, dY = (axis_movement(x_start, x_start, w, distance),
              axis_movement(y_start, y_start, h, distance))
    exclusions = generate_directions(dX, dY, distance)

    dX, dY = (axis_movement(x_start, x_end, w, distance),
              axis_movement(y_start, y_end, h, distance))
    directions = generate_directions(dX, dY, distance, exclusions)

    return len(directions)