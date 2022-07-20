import heapq

INF = 1e30

# 다익스트라 알고리즘(우선 순위 큐), 비트마스크 활용
def solution(n, start, end, roads, traps):
    answer = INF
    min_cost = [[INF for _ in range(n+1)] for _ in range(2**len(traps))]
    traps = {v: i for i, v in enumerate(traps)}
    graph = [[] for _ in range(n+1)]
    for P, Q, S in roads:
        graph[P].append([Q, S, True])
        graph[Q].append([P, S, False])
    
    q = []
    heapq.heappush(q, [0, start, 0])
    min_cost[0][start] = 0
    
    while q:
        total, cur, state = heapq.heappop(q)
        if cur == end:
            answer = min(answer, total)
            continue
        if total > min_cost[state][cur]:
            continue
        for next, cost, flag in graph[cur]:
            is_cur_traps_on = (state & (1 << traps[cur])) > 0 if cur in traps else False
            is_next_traps_on = (state & (1 << traps[next])) > 0 if next in traps else False
            if flag == (is_cur_traps_on != is_next_traps_on):
                continue
                
            next_state = state ^ (1 << traps[next]) if next in traps else state
            next_total = total + cost
            if next_total <= min_cost[next_state][next]:                
                min_cost[next_state][next] = next_total
                heapq.heappush(q, [next_total, next, next_state])
        
    return answer