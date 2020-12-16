with open('input', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
            
ranges = {}
part = 1
error_rate = 0
ticket = []
valid_tickets = []
cols = 0
for line in lines:
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
        #print(f"tag={tag}, ranges[tag]={ranges[tag]}")
        continue
    if part == 2:
        ticket = [int(n) for n in line.replace(',', ' ').split()]
        continue
    if part == 3:
        numbers = [int(n) for n in line.replace(',', ' ').split()]
        cols = len(numbers)
        all_valid = True        
        for n in numbers:
            valid = False
            for r in ranges.values():
                if ((n >= r[0]) and (n <= r[1])) or ((n >= r[2]) and (n <= r[3])):
                    valid = True
                    break
            if not valid:
                error_rate += n
                all_valid = False
        if all_valid:
            valid_tickets.append(numbers)
print(f"error_rate: {error_rate}")
print(f"ticket: {ticket}")
#print(f"valid tickets: {valid_tickets}")

possibles = [[] for i in range(cols)]
for i in range(cols):
    for k in ranges.keys():
        r = ranges[k]
        #print(f"looking at range {k}:{r} for slot {i}")
        is_possible = True
        for t in valid_tickets:
            n = t[i]
            if ((n < r[0]) or (n > r[1])) and ((n < r[2]) or (n > r[3])):
                is_possible = False
                #print(f"rejecting {n}")
                break
        if is_possible:
            possibles[i].append(k)
            #print(f"{k} is possible for {i}")

while True:
    has_more = False 
    for i in range(cols):
        candidates = possibles[i]
        if len(candidates) > 1:
            has_more = True
        else:
            for j in range(cols):
                if j == i:
                    continue
                candidate = candidates[0]
                if candidate in possibles[j]:
                    possibles[j].remove(candidate)
    if not has_more:
        break
#print("candidates are now:")        
#for candidate in possibles:
#    print(f"{candidate}")
product = 1
for i in range(cols):
    if possibles[i][0].startswith('departure'):
        print(f"adding {possibles[i][0]} = {ticket[i]}")
        product *= ticket[i]        
print(product)  