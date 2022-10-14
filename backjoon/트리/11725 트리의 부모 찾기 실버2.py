import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import defaultdict
n = int(input())

parent = [0] * (n + 1)
visited = [False] * (n + 1)
tree = defaultdict(list)

def dfs(cur):
    visited[cur] = True
    for i in range(len(tree[cur])):
        next = tree[cur][i]
        if not visited[next]:
            parent[next] = cur
            dfs(next)

for _ in range(n - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
dfs(1)
for i in range(2, n + 1):
    print(parent[i])