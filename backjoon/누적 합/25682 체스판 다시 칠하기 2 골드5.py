import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
dic = {0:'B', 1:'W'}
answer = 10**7
for h in range(2):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            val = (i + j + h) % 2
            if dic[val] != board[i][j]:
                dp[i + 1][j + 1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] += dp[i][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] += dp[i - 1][j]

    for i in range(n - k + 1):
        for j in range(m - k + 1):
            cur = dp[i][j] - dp[i + k][j] - dp[i][j + k] + dp[i + k][j + k]
            answer = min(answer, cur)
print(answer)