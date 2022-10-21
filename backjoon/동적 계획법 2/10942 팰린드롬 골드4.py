import sys
input = sys.stdin.readline
n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = True
for diagonal in range(1, n):
    for i in range(1, n - diagonal + 1):
        j = i + diagonal
        if dp[i + 1][j - 1] or diagonal == 1:
            dp[i][j] = (nums[i] == nums[j])
    
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(1 if dp[s][e] else 0)