import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
arr = [[INF] * v for _ in range(v)]

for i in range(v):
    arr[i][i] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a - 1][b - 1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

answer = INF
for i in range(v):
    for j in range(i + 1, v):
        answer = min(answer, arr[i][j] + arr[j][i])
print(answer if answer != INF else -1)