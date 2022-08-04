import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [a[0]]

def find(i):
    low, high = 0, len(dp) - 1
    while low <= high:
        mid = (low + high) // 2
        if dp[mid] == i:
            return mid
        elif dp[mid] < i:
            low = mid + 1
        else:
            high = mid - 1
    return low

for i in a:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[find(i)] = i
print(len(dp))

# from bisect import bisect_left
# import sys
# input = sys.stdin.readline
# n = int(input())
# a = list(map(int, input().split()))
# dp = [a[0]]

# for i in a:
#     if dp[-1] < i:
#         dp.append(i)
#     else:
#         dp[bisect_left(dp, i)] = i
# print(len(dp))