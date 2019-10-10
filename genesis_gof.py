import pygame
from pygame import *
import random
import numpy as np


# initialize constants
cell_size = 15
grey = (30, 30, 30)
screen_x = 800
screen_y = 800
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
FPS = 10
thresh_hold = .90
height = int(screen_y/cell_size)
width = int(screen_x/cell_size)
dead_state = np.zeros((height, width))
next_board_state = np.array((height, width))

# function to initialize the states; namely randomly here; takes dead state as argument


def init_state(dead_state):
    initial_state = dead_state
    for i in range(height):
        for j in range(width):
            rand = random.random()
            if rand > thresh_hold:
                initial_state[i][j] = 1
            else:
                initial_state[i][j] = 0
    return initial_state


# function to take a state and render it onto a display
def render_state(array, display_game):
    for i in range(height):
        for j in range(width):
            try:
                if array[i][j] == 1:
                    display_game.fill(white, rect=[i*cell_size, j*cell_size, cell_size, cell_size])
                elif array[i][j] == 0:
                    display_game.fill(black, rect=[i * cell_size, j * cell_size, cell_size, cell_size])

            except IndexError:
                display_game.fill(black, rect=[i * cell_size, j * cell_size, cell_size, cell_size])
            pygame.draw.rect(display_game, grey, [i * cell_size, j * cell_size, cell_size, cell_size], 1)

# function that calculates the next state given a initial state


def next_state(initial_state):
    next_board_state = initial_state
    for i in range(height):
        for j in range(width):
            alive_count = get_neighbours_count(i, j, initial_state)
            if initial_state[i][j] == 1:
                if alive_count == 0 or alive_count == 1:
                    next_board_state[i][j] = 0
                elif alive_count == 2 or alive_count == 3:
                    next_board_state[i][j] = 1
                elif alive_count > 3:
                    next_board_state[i][j] = 0
            else:
                if alive_count == 3:
                    next_board_state[i][j] = 1
                else:
                    next_board_state[i][j] = 0
    return next_board_state


# calculates the no. of live cells in the neighbourhood of a given state and cell
def get_neighbours_count(i, j, array):
    x = np.array([i-1, i, i+1], int)
    y = np.array([j-1, j, j+1], int)
    alive_count = 0
    for k in range(3):
        if x[k] < 0 or x[k] > height-1:
            continue
        for l in range(3):
            if y[l] < 0 or y[l] > width-1:
                continue
            if x[k] == i and y[l] == j:
                continue
            if array[x[k]][y[l]] == 1:
                alive_count += 1
    return alive_count


def handleInputEvents():
    exitGame = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
    return exitGame


def load_board_state(file):
    with open(file, 'r') as f:
        initial_state = f.read()
    return initial_state


def start_game():
    # initialize pygame window and set clock to keep timer.
    x = pygame.init()
    clock = pygame.time.Clock()

    # the window size setup, title, background color.

    display_game = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Genetic Game of Life")
    display_game.fill(white, rect=[0, 0, height*cell_size,width*cell_size])

    # initialize each cell state with random state either dead or alive

    initial_state = init_state(dead_state)

    # render random states on to the board
    render_state(initial_state, display_game)
    pygame.display.update()

    while True:
        next_board_state = next_state(initial_state)
        clock.tick(40)
        render_state(next_board_state, display_game)
        pygame.display.update()
        initial_state = next_board_state
        if handleInputEvents():
            break
# Quit on close button press
    pygame.quit()
    quit()


if __name__ == '__main__':
    start_game()


