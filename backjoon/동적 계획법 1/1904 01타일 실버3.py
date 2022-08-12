n = int(input())
dp = [1, 2, 3]
for i in range(3, n):
    dp.append((dp[-1] + dp[-2]) % 15746)
print(dp[n - 1])