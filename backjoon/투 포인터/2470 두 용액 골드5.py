import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
left, right = 0, n - 1
l, r = a[0], a[-1]
prev = abs(l + r)
while left < right:
    cur = a[left] + a[right]
    if abs(cur) < prev:
        l, r = a[left], a[right]
        prev = abs(cur)
    if cur < 0:
        left += 1
    elif cur > 0:
        right -= 1
    else:
        left += 1
        right -= 1
print(l, r)