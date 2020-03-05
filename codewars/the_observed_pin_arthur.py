# aurthor: Arthur
# date: 2018.12.28

from functools import reduce

# initialize approximation table
raw_panel = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['', '0', ''],
]

panel = [['' for j in range(len(raw_panel[0]) + 2)]] + [[''] + row + [''] for row in raw_panel] + [['' for i in range(len(raw_panel[0]) + 2)]]

num_table = dict()
for y in range(1, len(panel) - 1):
    for x in range(1, len(panel[y]) - 1):
        if panel[y][x]:
            num_table[panel[y][x]] = [num for num in (panel[y][x + 1], panel[y][x - 1], panel[y + 1][x], panel[y - 1][x], panel[y][x]) if num]


def get_pins(observed):
    """ Use reduce function to calculate all chained combinations """
    def two_step_combine(list1, list2):
        return [i+j for i in list1 for j in list2]

    possible_nums_matrix = [num_table[num] for num in observed]
    return reduce(two_step_combine, possible_nums_matrix)
