n = int(input())
l = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [0] * n
for i in range(n):
    for j in range(i):
        if l[i][1] > l[j][1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(n - max(dp))