import sys
input = sys.stdin.readline

s = input().strip()
dp = [[0] * 26]
dp[0][ord(s[0]) - 97] = 1
for i in range(1, len(s)):
    dp.append(dp[-1][:])
    dp[i][ord(s[i]) - 97] += 1
for _ in range(int(input())):
    a, l, r = input().split()
    l, r = int(l), int(r)
    if l == 0:
        print(dp[r][ord(a) - 97])
    else:
        print(dp[r][ord(a) - 97] - dp[l - 1][ord(a) - 97])