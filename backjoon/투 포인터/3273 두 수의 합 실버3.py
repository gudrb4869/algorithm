import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())
answer = 0
left, right = 0, n - 1
while left < right:
    if a[left] + a[right] == x:
        answer += 1
        left += 1
        right -= 1
    elif a[left] + a[right] > x:
        right -= 1
    else:
        left += 1
print(answer)