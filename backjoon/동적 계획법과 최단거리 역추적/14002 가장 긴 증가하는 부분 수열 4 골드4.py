import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [[1, [a[i]]] for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[j][0] + 1 > dp[i][0]:
            dp[i][0] = dp[j][0] + 1
            dp[i][1] = dp[j][1] + [a[i]]
k = 0
for i in range(n):
    if dp[k][0] < dp[i][0]:
        k = i

print(dp[k][0])
print(*dp[k][1])