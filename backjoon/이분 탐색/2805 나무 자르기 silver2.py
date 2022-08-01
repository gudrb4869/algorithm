import sys
input = sys.stdin.readline
_, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))
low, high = 0, tree[-1]
answer = 0
while low <= high:
    mid = (low + high) // 2
    total = sum(t - mid if t > mid else 0 for t in tree)
    if total >= m:
        low = mid + 1
        answer = max(answer, mid)
    else:
        high = mid - 1
print(answer)