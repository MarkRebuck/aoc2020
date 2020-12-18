with open('input', 'r') as file:
    lines = ["".join(line.strip().split()) for line in file if line.strip()]

def precedence(c):
    if c == '*':
        return 1
    if c == '+':
        return 2
    return 0

total = 0
for line in lines:
    val = 0
    stack = ['.']
    post = ""
    for c in line:
        if c in '0123456789':
            post += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] not in ".(":
                post += stack.pop()
            if stack[-1] != '.':
                stack.pop()
        else:
            if precedence(c) > precedence(stack[-1]):
                stack.append(c)
            else:
                while precedence(c) <= precedence(stack[-1]):
                    post += stack.pop()
                stack.append(c)

    while stack[-1] != '.':
        post += stack.pop()

    print(post)
    stack = []
    for c in post:
        if c == '+':
            inc = stack.pop() + stack.pop()
            stack.append(inc)
        elif c == '*':
            inc = stack.pop() * stack.pop()
            stack.append(inc)
        else:
            stack.append(int(c))
        print(f"after {c}: stack={stack}")
    val = stack[0]
    print(val)
    total += val
print(f"total = {total}")
