def solution(n, times):
    answer = 1e18
    left, right = 0, n * max(times)
    while left <= right:
        mid = (left + right) // 2
        total_num = sum(mid // time for time in times)
        if total_num >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    return answer