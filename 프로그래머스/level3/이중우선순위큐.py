import heapq

def solution(operations):
    queue = []
    for operation in operations:
        cmd, v = operation.split()
        if cmd == 'I':
            heapq.heappush(queue, int(v))
        elif cmd == 'D' and queue:
            if v =='1':
                heapq._heapify_max(queue)
                heapq._heappop_max(queue)
            else:
                heapq.heapify(queue)
                heapq.heappop(queue)
    return [max(queue), min(queue)] if queue else [0, 0]