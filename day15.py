with open('input', 'r') as file:
    numbers = [int(n) for n in file.read().replace(',', ' ').split()]

spoken = 0
lasts = [[0] for _ in range(30000000)]
for i in range(30000000):
    if i < len(numbers):
        n = numbers[i]
        lasts[n].append(i+1)
        spoken = n
    else:
        last = lasts[spoken]
        spoken = 0 if len(last) < 3 else last[-1] - last[-2]
        lasts[spoken].append(i+1)
print(spoken)
