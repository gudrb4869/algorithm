import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(3):
        l[i][j] += min(l[i - 1][(j + 1) % 3], l[i - 1][(j - 1) % 3])
print(min(l[-1]))