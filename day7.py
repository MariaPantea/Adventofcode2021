from utils import read_input_as_one_line_ints
from collections import Counter


def get_fuel(x, y, is_part1):
    if is_part1:
        return abs(x - y)
    else:
        n = abs(x - y)
        return n*(n+1)//2


def get_best_fuel_consumption(is_part1):
    min_fuel_cells = 100000000

    for p in range(min_position, max_position):
        fuel_cells = 0
        for i in crabs.keys():
            fuel = get_fuel(i, p, is_part1)
            fuel_cells += crabs[i] * fuel

        if fuel_cells < min_fuel_cells:
            min_fuel_cells = fuel_cells

    return min_fuel_cells


if __name__ == '__main__':
    data = read_input_as_one_line_ints('inputs/day7.txt')
    max_position = max(data)
    min_position = min(data)
    crabs = dict(Counter(data))

    print('Part 1: ', get_best_fuel_consumption(is_part1=True))
    print('Part 2: ', get_best_fuel_consumption(is_part1=False))
