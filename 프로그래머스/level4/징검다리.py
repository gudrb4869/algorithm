def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    low, high = 0, distance
    
    while low <= high:
        mid = (low + high) // 2
        prev, cnt = 0, 0
            
        for rock in rocks:
            if rock - prev < mid:
                cnt += 1
            else:
                prev = rock
            if cnt > n:
                break
        
        if cnt > n:
            high = mid - 1
        else:
            low = mid + 1
            answer = mid
        
    return answer