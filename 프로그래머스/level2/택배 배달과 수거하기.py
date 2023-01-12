def solution(cap, n, deliveries, pickups):
    answer = 0
    d, p = 0, 0
    for i in range(n - 1, -1, -1):
        if deliveries[i] == 0 and pickups[i] == 0:
            continue
        cnt = 0
        while d < deliveries[i] or p < pickups[i]:
            cnt += 1
            d += cap
            p += cap
        d -= deliveries[i]
        p -= pickups[i]
        answer += (i + 1) * cnt * 2
    return answer