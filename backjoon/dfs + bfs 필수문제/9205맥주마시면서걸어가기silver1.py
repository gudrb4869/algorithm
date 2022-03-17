import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    q =deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        if abs(ex - x) + abs(ey - y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visit[i]:
                nx, ny = conv[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append((nx, ny))
                    visit[i] = 1
    print('sad')

t=int(input())
for _ in range(t):
    n = int(input())
    sx, sy = list(map(int, input().split()))
    conv = []
    for _ in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])
    ex, ey = list(map(int, input().split()))
    visit = [0 for i in range(n + 1)]
    bfs()