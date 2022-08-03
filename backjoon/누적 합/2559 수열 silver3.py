n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = -int(1e7)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + arr[i - 1]
for i in range(k, n + 1):
    answer = max(answer, dp[i] - dp[i - k])
print(answer)