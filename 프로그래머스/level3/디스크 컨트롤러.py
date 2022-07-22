import heapq as hq

def solution(jobs):
    answer = 0
    hq.heapify(jobs)
    queue = []
    n = len(jobs)
    cur_time = 0
    
    while jobs or queue:
        while jobs and jobs[0][0] <= cur_time:
            r, e = hq.heappop(jobs)
            hq.heappush(queue, (e, r))
            
        if not queue:
            requested, elapsed = hq.heappop(jobs)
            cur_time += requested - cur_time
        else:
            elapsed, requested = hq.heappop(queue)

        cur_time += elapsed
        answer += cur_time - requested
    
    return answer // n