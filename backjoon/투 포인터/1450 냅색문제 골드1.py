# 투 포인터, Meet in the Middle 알고리즘
from bisect import bisect_right
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
w = list(map(int, input().split()))
a, b = w[:n//2], w[n//2:]
suma, sumb = [], []

def combine(arr, sumarr, l, w):
    if l >= len(arr):
        sumarr.append(w)
        return
    combine(arr, sumarr, l + 1, w)
    combine(arr, sumarr, l + 1, w + arr[l])

combine(a, suma, 0, 0)
combine(b, sumb, 0, 0)
sumb.sort()

answer = 0
for i in suma:
    if c - i >= 0:
        answer += bisect_right(sumb, c - i)
print(answer)