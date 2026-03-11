import random
import msvcrt

def start_game():
    mat = [[0] * 4 for _ in range(4)]
    add_new_tile(mat)
    add_new_tile(mat)
    return mat

def add_new_tile(mat):
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    while mat[a][b] != 0:
        a = random.randint(0, 3)
        b = random.randint(0, 3)
    mat[a][b] = 2 if random.random() < 0.9 else 4

def compress(mat):
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
    return mat

def move_left(grid):
    new_grid = compress(grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    return new_grid

def move_right(grid):
    reversed_grid = [row[::-1] for row in grid]
    moved_grid = move_left(reversed_grid)
    return [row[::-1] for row in moved_grid]

def move_up(grid):
    transposed_grid = [list(row) for row in zip(*grid)]
    moved_grid = move_left(transposed_grid)
    return [list(row) for row in zip(*moved_grid)]

def move_down(grid):
    transposed_grid = [list(row) for row in zip(*grid)]
    moved_grid = move_right(transposed_grid)
    return [list(row) for row in zip(*moved_grid)]

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048: return 'WON'
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0: return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return 'GAME NOT OVER'
    return 'LOST'

# Main Game Loop
mat = start_game()
while True:
    for row in mat: print(row)
    print("Press W/A/S/D to move: ", end='', flush=True)
    key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
    print()
    
    if key == 'w': mat = move_up(mat)
    elif key == 's': mat = move_down(mat)
    elif key == 'a': mat = move_left(mat)
    elif key == 'd': mat = move_right(mat)
    else: continue

    add_new_tile(mat)
    state = get_current_state(mat)
    if state != 'GAME NOT OVER':
        print(state)
        break