import numpy as np
from genesis_gof import *


def get_neighbours_count(i, j, array):
    x = np.array([i-1, i, i+1], int)
    y = np.array([j-1, j, j+1], int)
    alive_count = 0
    for k in range(3):
        if x[k] < 0 or x[k] >= height:
            continue
        for l in range(3):
            if y[l] < 0 or y[l] >= width:
                pass
            if x[k] == i and y[l] == j:
                continue
            if array[x[k]][y[l]] == 1:
                alive_count += 1
    return alive_count


def load_board_state(file):
    with open(file, 'r') as f:
        initial_state = f.read()
        print(initial_state)


if __name__ == '__main__':
    init_state = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]])
    print(next_state(init_state))
