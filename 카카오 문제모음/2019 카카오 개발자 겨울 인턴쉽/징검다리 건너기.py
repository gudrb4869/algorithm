def solution(stones, k):
    left, right = 1, max(stones)
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        for stone in stones:
            if stone <= mid:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
        if cnt < k:
            left = mid + 1
        else:
            right = mid - 1
    return left
