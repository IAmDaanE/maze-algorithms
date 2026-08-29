import pygame
import random
import json

WINDOW_WIDTH = 603
WINDOW_HEIGHT = 603

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Recursive Backtracker")
clock = pygame.time.Clock()

maze_color = (0,255,0)
snake_color = (0,85,0)
background_color = (0,0,0)
head_color = (255,255,255)
running = True
complete = False
data_dumped = False

rows = 30
columns = 30
walls_left = []
walls_top = []

moves = ["top", "right", "bottom", "left"]

visited_cells = set()
current_snake = []
current_cell = [random.randint(0,29),random.randint(0,29)]
visited_cells.add(tuple(current_cell))

for i in range(rows):
    walls_left.append([True] * columns)
    walls_top.append([True] * columns)

def can_go_top(row, column):
    if row == 0:
        return False
    elif walls_top[row][column]:
        if (current_cell[0] - 1, current_cell[1]) in visited_cells:
            return False
        else:
            return True
    else:
        return False

def can_go_bottom(row, column):
    if row == 29:
        return False
    elif walls_top[row + 1][column]:
        if (current_cell[0] + 1, current_cell[1]) in visited_cells:
            return False
        else:
            return True
    else:
        return False
    
def can_go_left(row, column):
    if column == 0:
        return False
    elif walls_left[row][column]:
        if (current_cell[0], current_cell[1] - 1) in visited_cells:
            return False
        else:
            return True
    else:
        return False

def can_go_right(row, column):
    if column == 29:
        return False
    elif walls_left[row][column + 1]:
        if (current_cell[0], current_cell[1] + 1) in visited_cells:
            return False
        else:
            return True
    else:
        return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not complete:
        random.shuffle(moves)
        moved = False
        for move in moves:
            if move == "top" and can_go_top(current_cell[0], current_cell[1]):
                walls_top[current_cell[0]][current_cell[1]] = False
                current_cell[0] -= 1
                visited_cells.add(tuple(current_cell))
                current_snake.append(current_cell[:])
                moved = True
            elif move == "right" and can_go_right(current_cell[0], current_cell[1]):
                current_cell[1] += 1
                walls_left[current_cell[0]][current_cell[1]] = False
                visited_cells.add(tuple(current_cell))
                current_snake.append(current_cell[:])
                moved = True
            elif move == "bottom" and can_go_bottom(current_cell[0], current_cell[1]):
                current_cell[0] += 1
                walls_top[current_cell[0]][current_cell[1]] = False
                visited_cells.add(tuple(current_cell))
                current_snake.append(current_cell[:])
                moved = True
            elif move == "left" and can_go_left(current_cell[0], current_cell[1]):
                walls_left[current_cell[0]][current_cell[1]] = False
                current_cell[1] -= 1
                visited_cells.add(tuple(current_cell))
                current_snake.append(current_cell[:])
                moved = True
            if moved:
                break
        if not moved:
            if len(current_snake) > 0:
                current_snake.pop()
                if len(current_snake) > 0:
                    current_cell = current_snake[-1]
                else:
                    complete = True
            else:
                complete = True
    
    if not data_dumped and complete:
        save_data = {"left_walls": walls_left, "top_walls": walls_top}
        with open("maze.json", "w") as f:
            json.dump(save_data, f)
        data_dumped = True

    screen.fill(background_color)

    if len(current_snake) > 0:
        #for row, column in current_snake:
        #    pygame.draw.rect(screen, snake_color, (column * 20, row * 20, 20, 20))
        #pygame.draw.rect(screen, snake_color, (1,1,20,20))
        pygame.draw.rect(screen, head_color, (current_cell[1] * 20, current_cell[0] * 20, 20, 20))

    for row in range(30):
        for column in range(30):
            x,y = column * 20, row * 20
            if walls_left[row][column]:
                pygame.draw.rect(screen, maze_color, (x,y,3,20))
            if walls_top[row][column]:
                pygame.draw.rect(screen, maze_color, (x,y,20,3))

    pygame.draw.rect(screen, maze_color, (600, 0, 3, 600))
    pygame.draw.rect(screen, maze_color, (0, 600, 600, 3))

    pygame.display.update()

    pygame.time.delay(0)