import re
import os
import time
from pickle import TRUE

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

ranges = {}
part = 1
error_rate = 0
for line in lines:
    if len(line.strip()) == 0:
        continue
    if "your ticket" in line:
        part = 2
        continue
    if "nearby tickets" in line:
        part = 3
        continue    
    if part == 1:
        pieces = line.split(':')
        tag = pieces[0]
        vals = pieces[1].strip().split(" or ")
        p1 = vals[0].split('-')
        p2 = vals[1].split('-')
        ranges[tag] = [int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])]
        print(f"tag={tag}, ranges[tag]={ranges[tag]}")
        continue
    if part == 3:
        numbers = [int(n) for n in line.replace(',', ' ').split()]        
        for n in numbers:
            found = False
            for r in ranges.values():
                if ((n >= r[0]) and (n <= r[1])) or ((n >= r[2]) and (n <= r[3])):
                    found = True
                    break
            if not found:
                error_rate += n
print(error_rate)                
                
        
    
    
    