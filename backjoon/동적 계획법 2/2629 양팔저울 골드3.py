dp = [[0] * 55001 for _ in range(31)]
n = int(input())
weight = [0] + list(map(int, input().split()))
sum = 0
for i in range(1, n + 1):
    dp[i][weight[i]] = 1
    sum += weight[i]
    for j in range(1, sum + 1):
        if dp[i - 1][j]:
            dp[i][j] = 1
            dp[i][j + weight[i]] = 1
            dp[i][abs(j - weight[i])] = 1

int(input())
marbles = list(map(int, input().split()))
result = []
for marble in marbles:
    result.append('Y' if dp[n][marble] else 'N')
print(*result)