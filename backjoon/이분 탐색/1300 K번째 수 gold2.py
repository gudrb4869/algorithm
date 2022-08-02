n = int(input())
k = int(input())
low, high = 1, k
answer = 0
while low <= high:
    mid = (low + high) // 2
    total = 0
    for i in range(1, n + 1):
        total += min(mid // i, n)
    if total < k:
        low = mid + 1
    else:
        answer = mid
        high = mid - 1
print(answer)