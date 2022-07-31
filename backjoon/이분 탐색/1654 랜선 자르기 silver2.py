k, n = map(int, input().split())
arr = sorted([int(input()) for _ in range(k)])
low, high = 1, max(arr)
answer = 1
while low <= high:
    mid = (low + high) // 2
    total = sum(a//mid for a in arr)
    if total >= n:
        low = mid + 1
        answer = max(answer, mid)
    else:
        high = mid - 1
print(answer)