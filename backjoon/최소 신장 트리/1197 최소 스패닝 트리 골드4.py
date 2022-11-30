'''
# Kruskal Algorithm
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
edges = []
for _ in range(e):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x:x[2])

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

answer = 0
for x, y, w in edges:
    a = find(x)
    b = find(y)
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        answer += w
print(answer)
'''

# Prim Algorithm
import sys, heapq
input = sys.stdin.readline
v, e = map(int, input().split())
visited = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
heap = [[0, 1]]
for _ in range(e):
    x, y, w = map(int, input().split())
    graph[x].append((w, y))
    graph[y].append((w, x))

answer = 0
count = 0
while heap:
    if count == v:
        break
    w, x = heapq.heappop(heap)
    if not visited[x]:
        visited[x] = True
        answer += w
        count += 1
        for w, y in graph[x]:
            heapq.heappush(heap, (w, y))
print(answer)