from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
buffer = deque(maxlen=n)

while True:
    x = int(input())
    if x == -1:
        break
    elif x == 0:
        buffer.popleft()
    else:
        if len(buffer) < n:
            buffer.append(x)

if buffer:
    print(*buffer)
else:
    print('empty')