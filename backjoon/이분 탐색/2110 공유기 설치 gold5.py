import sys
input = sys.stdin.readline
n, c  = map(int, input().split())
x = sorted([int(input()) for _ in range(n)])
low, high = 0, x[-1]
answer = 0
while low <= high:
    mid = (low + high) // 2
    prev, cnt = x[0], 1
    for i in x[1:]:
        if i - prev >= mid:
            cnt += 1
            prev = i

    if cnt < c:
        high = mid - 1
    else:
        low = mid + 1
        answer = mid
print(answer)