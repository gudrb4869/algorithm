import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
dp = [num[0]]
cur = num[0]
for i in range(1, n):
    dp.append(max(num[i], dp[-1] + num[i]))
print(max(dp))