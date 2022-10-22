import sys
input = sys.stdin.readline
N, M = map(int, input().split())
m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
answer = total = sum(c)
dp = [[0] * (total + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, total + 1):
        if j >= c[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c[i]] + m[i])
        else:
            dp[i][j] = dp[i - 1][j]
        if dp[i][j] >= M:
            answer = min(answer, j)
print(answer)