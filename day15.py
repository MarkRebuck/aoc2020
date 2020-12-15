import re
import os
import time

with open('input', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
    words = [line.split() for line in lines]
    board = [list(line.strip()) for line in lines]
    board_flat = sum(board, [])
numbers = []
try:
    with open('input', 'r') as file:
        numbers = [int(n) for n in file.read().replace(',', ' ').split()]
except:
    pass
            
print(f"lines: {lines}")
print(f"words: {words}")
print(f"board: {board}")
print(f"board_flat: {board_flat}")
print(f"numbers: {numbers}")

spoken = 0
lasts = [[0] for _ in range(30000000)]
for i in range(30000000):
    if i < len(numbers):
        n = numbers[i]
        lasts[n].append(i+1)
        spoken = n
    else:
        #print(f"spoken = {spoken}")
        last = lasts[spoken]
        if len(last) < 3:
            lasts[0].append(i+1)
            spoken = 0
        else:
            spoken = last[-1] - last[-2]
            lasts[spoken].append(i+1)
    #print(spoken)
print(spoken)    