S, E = input(), input()
length = len(E)
stack = []

for s in S:
    stack.append(s)
    if s == E[-1] and ''.join(stack[-length:]) == E:
        for _ in range(length):
            stack.pop()

print('FRULA' if not stack else ''.join(stack))