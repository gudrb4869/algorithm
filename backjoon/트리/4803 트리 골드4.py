import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    isTree = True
    q = deque([x])
    while q:
        i = q.popleft()
        if visited[i]:
            isTree = False
        visited[i] = 1
        for j in graph[i]:
            if not visited[j]:
                q.append(j)
    return isTree
    
t = 0
while True:
    t += 1
    n, m = map(int, input().split())
    if n == m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [0] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if not visited[i] and bfs(i):
            count += 1

    if count == 0:
        print('Case {}: No trees.'.format(t))
    elif count == 1:
        print('Case {}: There is one tree.'.format(t))
    else:
        print('Case {}: A forest of {} trees.'.format(t, count))