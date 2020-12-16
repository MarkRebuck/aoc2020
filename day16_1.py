with open('input', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
            
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
        #print(f"tag={tag}, ranges[tag]={ranges[tag]}")
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