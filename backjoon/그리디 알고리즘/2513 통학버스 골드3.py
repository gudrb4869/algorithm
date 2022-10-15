import heapq, sys
input = sys.stdin.readline

n, k, s = map(int, input().split())
L, R = [], []
for _ in range(n):
    a, b = map(int, input().split())
    if a <= s:
        heapq.heappush(L, (a, b))
    else:
        heapq.heappush(R, (-a, b))
answer = 0
bus = 0
dist = 0
while L:
    l, p = heapq.heappop(L)
    if (k - bus) >= p:
        bus += p
        dist = max(dist, s - l)
        if not L:
            answer += dist
    else:
        heapq.heappush(L, (l, p-(k-bus)))
        if dist == 0:
            answer += (s-l)
        else:
            answer += dist
            dist = 0
        bus = 0
bus = 0
dist = 0
while R:
    l, p = heapq.heappop(R)
    l = -l
    if (k - bus) >= p:
        bus += p
        dist = max(dist, l - s)
        if not R:
            answer += dist
    else:
        heapq.heappush(R, (-l, p-(k-bus)))
        if dist == 0:
            answer += (l-s)
        else:
            answer += dist
            dist = 0
        bus = 0
print(answer * 2)