import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))

def dfs(x):
    for y, w in graph[x]:
        if distance[y] == -1:
            distance[y] = distance[x] + w
            dfs(y)

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1)

x = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[x] = 0
dfs(x)

print(max(distance))