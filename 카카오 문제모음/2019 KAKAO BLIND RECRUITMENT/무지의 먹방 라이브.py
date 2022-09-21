import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
        
    time = k
    length = len(q)
    prev = 0
    while (q[0][0] - prev) * length <= time:
        now = heapq.heappop(q)[0]
        time -= (now - prev) * length
        length -= 1
        prev = now
        
    return sorted(q, key=lambda x: x[1])[time % length][1]