import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
parent = [i for i in range(n + 1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a > b:
        a, b = b, a
    parent[b] = a

def isUnion(a, b):
    return find(a) == find(b)
    
for i in range(1, n + 1):
    graph[i] = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if graph[i][j]:
            union(i, j)
path = list(map(int, input().split()))
start = path[0]
check = True
for p in path:
    check &= isUnion(start, p)
print('YES' if check else 'NO')