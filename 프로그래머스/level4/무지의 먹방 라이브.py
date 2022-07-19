import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    time, previous = 0, 0
    length = len(food_times)
    
    while time + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        time += (now - previous) * length
        length -= 1
        previous = now
        
    result = sorted(q, key=lambda x:x[1])
    return result[(k - time) % length][1] if result else -1