import copy
import pandas as pd
import numpy as np
import io

with open('input', 'r') as file:
    lines = [line.strip().replace("#","1\t").replace(".","0\t") for line in file if line.strip()]
df = pd.read_csv(io.StringIO('\n'.join(lines)), header=None, delim_whitespace=True)
initial = df.to_numpy()

runs = 6

initial_size = initial[0].shape[0] 
layer_size = initial_size + (2 * runs)
stack_size = 1 + (2 * runs)
board = np.zeros([stack_size, stack_size, layer_size, layer_size], dtype='int') 
mid = (int)(stack_size / 2)
for x in range(initial_size):
    for y in range(initial_size):
        board[mid][mid][y+runs][x+runs] = initial[y][x]
#print(f"initial:\n{board}")

boards = [board, copy.deepcopy(board)]
current = 0
for n in range(runs):
    board = boards[current]
    new_board = boards[1 - current]
 
    for z in range(stack_size):
        for w in range(stack_size):
            for x in range(layer_size):
                for y in range(layer_size):
                    neighbors = 0
                    for xp in [x - 1, x, x + 1]:
                        for yp in [y - 1, y, y + 1]:
                            for zp in [z - 1, z, z + 1]:
                                for wp in [w - 1, w, w + 1]:
                                    if (xp == x) and (yp == y) and (zp == z) and (wp == w):
                                        continue
                                    if (xp < 0) or (yp < 0) or (zp < 0) and (wp < 0):
                                        continue
                                    if (xp >= layer_size) or (yp >= layer_size) or (zp >= stack_size) or (wp >= stack_size):
                                        continue
                                    c = board[zp][wp][xp][yp]
                                    if c == 1:
                                        neighbors += 1
                    c = board[z][w][x][y]                                
                    if c == 1:
                        new_board[z][w][x][y] = 1 if (neighbors == 2) or (neighbors == 3) else 0
                    if c == 0:
                        new_board[z][w][x][y] = 1 if (neighbors == 3) else 0
    current = 1 - current

board = boards[current]
#print(f"final:{board}")
active = 0
for layer in board:
    active += layer.sum()
print(active)
