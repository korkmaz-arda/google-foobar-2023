from itertools import combinations


def solution(num_buns, num_required):
    if num_buns < num_required:
        return []

    keys = [[] for _ in range(num_buns)]

    key_locations = list(combinations(range(num_buns), num_buns-num_required+1))
    for key, locations in enumerate(key_locations):
            for loc in locations:
                keys[loc].append(key)

    return keys