import sys
input = sys.stdin.readline
n = int(input())
w = [int(input()) for _ in range(n)]
if n <= 2:
    print(sum(w))
    exit(0)
d = [0] * (n + 1)
d[1], d[2] = w[0], w[0] + w[1]
for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 3] + w[i - 2] + w[i - 1], d[i - 2] + w[i - 1])
print(d[n])