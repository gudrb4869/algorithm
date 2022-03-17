from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
arr = {i for i in range(n)}
result = 10000
for r1 in combinations(arr, n // 2):
    start, link = 0, 0
    r2 = list(arr - set(r1))
    for r in combinations(r1, 2):
        start += s[r[0]][r[1]] + s[r[1]][r[0]]
    for r in combinations(r2, 2):
        link += s[r[0]][r[1]] + s[r[1]][r[0]]
    result = min(result, abs(start - link))
print(result)
