import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        a, b = b, a
    parent[b] = a

def isUnion(a, b):
    return find(a) == find(b)

for _ in range(m):
    x, a, b = map(int, input().split())
    print('YES' if isUnion(a, b) else 'NO') if x else union(a, b)