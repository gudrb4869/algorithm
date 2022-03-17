from collections import deque
n,k=map(int,input().split())
visit = [0] * 100001
q = deque([(n, 0)])
visit[n] = 1
while q:
    x, cur = q.popleft()
    if x == k:
        print(cur)
        exit(0)
    nxs = (x - 1, x + 1, x * 2)
    for nx in nxs:
        if 0 <= nx < 100001 and not visit[nx]:
            visit[nx] = 1
            q.append((nx, cur + 1))