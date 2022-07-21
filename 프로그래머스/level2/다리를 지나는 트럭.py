def solution(bridge_length, weight, truck_weights):
    time = 0
    n = len(truck_weights)
    queue, finish = [], []
    while len(finish) < n:
        time += 1
        if queue and time - queue[0][1] == bridge_length:
            finish.append(queue.pop(0)[0])        
        if truck_weights and sum(q[0] for q in queue) + truck_weights[0] <= weight:
            queue.append((truck_weights.pop(0), time))
        
    return time