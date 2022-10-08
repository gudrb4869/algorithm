n = int(input())
m = [[0] * (n + 1) for _ in range(n + 1)]
d = [0] * (n + 1)
for i in range(n):
    d[i], d[i + 1] = map(int, input().split())
for diagonal in range(1, n):
    for i in range(1, n - diagonal + 1):
        j = i + diagonal
        if i < j:
            m[i][j] = min([m[i][k] + m[k + 1][j] + d[i - 1] * d[k] * d[j] for k in range(i, j)])
print(m[1][n])