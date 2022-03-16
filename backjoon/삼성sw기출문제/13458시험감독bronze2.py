import math
import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, input().split())
answer = n
for i in range(n):
    a[i] -= b
    if a[i] <= 0:
        continue
    answer += math.ceil(a[i] / c)
print(answer)