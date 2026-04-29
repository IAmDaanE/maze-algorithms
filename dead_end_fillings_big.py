import pygame
import random
import json
import copy

WINDOW_WIDTH = 601
WINDOW_HEIGHT = 602

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dead end fillings")
clock = pygame.time.Clock()

maze_color = (0,255,0)
checked_cells_color = (0,85,0)
correct_path_color = (100,0,0)
background_color = (0,0,0)
running = True
complete = False
first_scan_done = False

rows = 100
columns = 100
rendered_walls_left = []
rendered_walls_top = []

with open("big_maze.json", "r") as f:
    raw_unloaded_data = json.load(f)
    rendered_walls_left = raw_unloaded_data["left_walls"]
    rendered_walls_top = raw_unloaded_data["top_walls"]

fake_walls_left = copy.deepcopy(rendered_walls_left)
fake_walls_top = copy.deepcopy(rendered_walls_top)
checked_cells = []
queue = []
opening_count = 0

def can_go_top(row, column):
    if row == 0:
        return 0
    elif fake_walls_top[row][column]:
        return 0
    else:
        return 1
    
def can_go_bottom(row, column):
    if row == 99:
        return 0
    elif fake_walls_top[row + 1][column]:
        return 0
    else:
        return 1
    
def can_go_left(row, column):
    if column == 0:
        return 0
    elif fake_walls_left[row][column]:
        return 0
    else:
        return 1

def can_go_right(row, column):
    if column == 99:
        return 0
    elif fake_walls_left[row][column + 1]:
        return 0
    else:
        return 1

def count_openings(row, column):
    global opening_count
    opening_count = 0
    opening_count += can_go_top(row, column)
    opening_count += can_go_right(row, column)
    opening_count += can_go_bottom(row, column)
    opening_count += can_go_left(row, column)
    return opening_count

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #---------------------------

    if not first_scan_done:
        for row in range(99, -1, -1):
            for column in range(100):
                if count_openings(row, column) <= 1 and (row,column) != (0,0) and (row,column) != (99,99):
                    queue.append([row, column])
        first_scan_done = True

    if not complete:
        row, column = queue.pop()
        checked_cells.append((row, column))
        if not fake_walls_top[row][column]:
            fake_walls_top[row][column] = True
        if row != 99:
            if not fake_walls_top[row + 1][column]:
                fake_walls_top[row + 1][column] = True
        if not fake_walls_left[row][column]:
            fake_walls_left[row][column] = True
        if column != 99:
            if not fake_walls_left[row][column + 1]:
                fake_walls_left[row][column + 1] = True
        if row != 0:
            if count_openings(row - 1, column) <= 1 and (row - 1, column) not in checked_cells and (row - 1, column) != (0,0) and (row - 1, column) != (99,99):
                queue.append([row - 1, column])
        if row != 99:
            if count_openings(row + 1, column) <= 1 and (row + 1, column) not in checked_cells and (row + 1, column) != (0,0) and (row + 1, column) != (99,99):
                queue.append([row + 1, column])
        if column != 0:
            if count_openings(row, column - 1) <= 1 and (row, column - 1) not in checked_cells and (row, column - 1) != (0,0) and (row, column - 1) != (99,99):
                queue.append([row, column - 1])
        if column != 99:
            if count_openings(row, column + 1) <= 1 and (row, column + 1) not in checked_cells and (row, column + 1) != (0,0) and (row, column + 1) != (99,99):
                queue.append([row, column + 1])

    if len(queue) == 0:
        complete = True
    #---------------------------
    screen.fill((0,0,0))
    for row, column in checked_cells:
        pygame.draw.rect(screen, checked_cells_color, (column * 6, row * 6, 6, 6))

    if complete:
        for row in range(100):
            for column in range(100):
                if (row,column) not in checked_cells:
                    pygame.draw.rect(screen, correct_path_color, (column * 6, row * 6, 6, 6))

    for row in range(100):
        for column in range(100):
            x,y = column * 6, row * 6
            if rendered_walls_left[row][column]:
                pygame.draw.rect(screen, maze_color, (x,y,1,6))
            if rendered_walls_top[row][column]:
                pygame.draw.rect(screen, maze_color, (x,y,6,1))
    pygame.draw.rect(screen, maze_color, (600, 0, 1, 600))
    pygame.draw.rect(screen, maze_color, (0, 600, 600, 1))

    pygame.display.update()

    pygame.time.delay(0)