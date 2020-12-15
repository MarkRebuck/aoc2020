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