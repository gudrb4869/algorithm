n = int(input())
lst = [[0, 0]] * (n + 1)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    t, p = map(int, input().split())
    lst[i] = [t, p]

for i in range(1, n + 1):
    if i + lst[i][0] - 1 < n + 1:
        dp[i + lst[i][0] - 1] = max(dp[i + lst[i][0] - 1], dp[i - 1] + lst[i][1])
    dp[i] = max(dp[i], dp[i - 1])
    print(dp)
print(dp[n])