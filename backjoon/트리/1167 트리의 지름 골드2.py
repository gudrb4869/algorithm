import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    x, *lst, _  = list(map(int, input().split()))
    for i in range(len(lst) // 2):
        y, w = lst[i * 2], lst[i * 2 + 1]
        graph[x].append((y, w))

def dfs(x):
    for y, w in graph[x]:
        if distance[y] == -1:
            distance[y] = distance[x] + w
            dfs(y)

distance = [-1] * (V + 1)
distance[1] = 0
dfs(1)

x = distance.index(max(distance))
distance = [-1] * (V + 1)
distance[x] = 0
dfs(x)

print(max(distance))