import math
    
with open('input', 'r') as file:
    pieces = file.read().split('\n\n')
print(pieces)
    
tiles = {}
for piece in pieces:
    tiles[int(piece[5:9])] = piece[11:].split('\n')
borders = {} 
border2tile = {}

for k in tiles.keys():
    tile = tiles[k]
    right = "".join([p[-1] for p in tile])
    left = "".join([p[0] for p in tile])
    border_list = [tile[0], tile[0][::-1], tile[-1], tile[-1][::-1], right, right[::-1], left, left[::-1]]
    borders[k] = border_list
    for b in border_list:
        s = set([])
        if b in border2tile:
            s = border2tile[b]
        s.add(k)
        border2tile[b] = s   

#  We got lucky here, and the outside edge borders appear
#  to be patterns not shared with any "interior/shared" borders.
#  So we can just look at the pieces which have the fewest "common"
#  borders.  Corners will only share two edges, while non-corner side
#  pieces will share 3, and interior pieces share 4.  If there are
#  four pieces with few shared borders, those are likely the corners.
#
#  The aoc designers could have made this harder by having outside
#  border share the same pattern as some inside borders :-).
shared_borders = {}
for k in tiles.keys():
    count = sum([len(border2tile[border]) for border in borders[k]])
    shared_borders[k] = count    
ordered = sorted(shared_borders.items(), key=lambda x: x[1])
print(math.prod([ordered[i][0] for i in range(4)]))