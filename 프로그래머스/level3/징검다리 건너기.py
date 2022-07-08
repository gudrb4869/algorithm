def solution(stones, k):
    left, right = 1, max(stones)
    
    while left <= right:    
        cnt = 0
        mid = (left + right) // 2
        for stone in stones:
            if stone <= mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt < k:
            left = mid + 1
        else:
            right = mid - 1
            
    return left
    # dp 이용시 효율성 통과 못함. 이진탐색 이용시 효율성 통과 가능.
    # n = len(stones)
    # dp = [0] * n
    # dp[0] = stones[0]
    
    # for i in range(1, k):
    #     dp[i] = max(dp[i - 1], stones[i])

    # for i in range(k, n):
    #     if stones[i] < dp[i - 1]:
    #         dp[i] = min(dp[i - 1], max([stones[i - j] for j in range(k)]))
    #     else:
    #         dp[i] = dp[i - 1]
    # return dp[n - 1]