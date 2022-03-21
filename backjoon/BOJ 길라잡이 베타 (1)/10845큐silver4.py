import sys
from collections import deque
input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    e = input().split()
    if e[0] == 'front':
        print(-1 if not q else q[0])
    elif e[0] == 'back':
        print(-1 if not q else q[-1])
    elif e[0] == 'size':
        print(len(q))
    elif e[0] == 'empty':
        print(1 if not q else 0)
    elif e[0] == 'pop':
        print(-1 if not q else q.popleft())
    else:
        q.append(e[1])
