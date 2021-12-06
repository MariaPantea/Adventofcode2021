from utils import read_input_as_one_line_ints
from collections import Counter


def update_fish(fish):
    new_fish = {}
    for k in range(8, -1, -1):
        v = fish.get(k, 0)
        if k == 0:
            new_fish[8] = v
            new_fish[6] = v + fish.get(7, 0)
        else:
            new_fish[k - 1] = v

    return new_fish


def evolve(days):
    fish = dict(Counter(data))
    for i in range(days):
        fish = update_fish(fish)

    return sum(fish.values())


data = read_input_as_one_line_ints('inputs/day6.txt')
print('Part 1: ', evolve(80))
print('Part 2: ', evolve(256))
