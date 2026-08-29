import pygame
import random
import json

WINDOW_WIDTH = 601
WINDOW_HEIGHT = 602

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wall Follower")
clock = pygame.time.Clock()

maze_color = (0,255,0)
snake_color = (0,85,0)
snake_complete_color = (100,0,0)
background_color = (0,0,0)
head_color = (255,255,255)
running = True
complete = False

rows = 100
columns = 100
walls_left = []
walls_top = []
moved = False

moves = []
direction_library = {"right": ["top", "right", "bottom", "left"],
                     "bottom": ["right", "bottom", "left", "top"],
                     "left": ["bottom", "left", "top", "right"],
                     "top": ["left", "top", "right", "bottom"]}
direction = "right"
moves = direction_library[direction]

current_snake = []
current_cell = [0,0]
current_snake.append(current_cell)

def can_go_top(row, column):
    if row == 0:
        return False
    elif walls_top[row][column]:
        return False
    else:
        return True

def can_go_bottom(row, column):
    if row == 99:
        return False
    elif walls_top[row + 1][column]:
        return False
    else:
        return True
    
def can_go_left(row, column):
    if column == 0:
        return False
    elif walls_left[row][column]:
        return False
    else:
        return True

def can_go_right(row, column):
    if column == 99:
        return False
    elif walls_left[row][column + 1]:
        return False
    else:
        return True

with open("big_maze.json", "r") as f:
    raw_unloaded_data = json.load(f)
    walls_left = raw_unloaded_data["left_walls"]
    walls_top = raw_unloaded_data["top_walls"]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #---------------------------

    if not complete:
        moved = False
        for move in moves:
            if move == "top":
                if can_go_top(current_cell[0], current_cell[1]):
                    current_cell[0] -= 1
                    current_snake.append(current_cell[:])
                    direction = "top"
                    moved = True
            elif move == "right":
                if can_go_right(current_cell[0], current_cell[1]):
                    current_cell[1] += 1
                    current_snake.append(current_cell[:])
                    direction = "right"
                    moved = True
            elif move == "bottom":
                if can_go_bottom(current_cell[0], current_cell[1]):
                    current_cell[0] += 1
                    current_snake.append(current_cell[:])
                    direction = "bottom"
                    moved = True
            elif move == "left":
                if can_go_left(current_cell[0], current_cell[1]):
                    current_cell[1] -= 1
                    current_snake.append(current_cell[:])
                    direction = "left"
                    moved = True
            if moved:
                break

        moves = direction_library[direction]
        if current_cell == [99, 99]:
            complete = True

    #---------------------------
    screen.fill((0,0,0))
    
    if len(current_snake) > 0:
        if not complete:
            for row, column in current_snake:
                pygame.draw.rect(screen, snake_color, (column * 6, row * 6, 6, 6))
            pygame.draw.rect(screen, snake_color, (1,1,6,6))
            pygame.draw.rect(screen, head_color, (current_cell[1] * 6, current_cell[0] * 6, 6, 6))
        else:
            for row, column in current_snake:
                pygame.draw.rect(screen, snake_complete_color, (column * 6, row * 6, 6, 6))
            pygame.draw.rect(screen, snake_complete_color, (1,1,6,6))
    
    for row in range(100):
        for column in range(100):
            x,y = column * 6, row * 6
            if walls_left[row][column]:
                pygame.draw.rect(screen, maze_color, (x,y,1,6))
            if walls_top[row][column]:
                pygame.draw.rect(screen, maze_color, (x,y,6,1))
    pygame.draw.rect(screen, maze_color, (600, 0, 1, 600))
    pygame.draw.rect(screen, maze_color, (0, 600, 600, 1))

    pygame.display.update()

    pygame.time.delay(0)