import sys
from itertools import combinations
input = sys.stdin.readline

def dst(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

n, m = map(int, input().split())
house, chicken = [], []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            house.append([i,j])
        elif arr[j] == 2:
            chicken.append([i,j])

ans = 999999
for ch in list(combinations(chicken, m)):
    cur = 0
    for h in house:
        dist = 2500
        for c in ch:
            dist = min(dist, dst(h, c))
        cur += dist
    ans = min(ans, cur)
print(ans)