from collections import deque
def bfs():
    q = deque()
    q.append(s)
    visited[s] = 1
    count[s] = 0
    while q:
        cur = q.popleft()
        if cur == g:
            print(count[cur])
            exit(0)
        for i in [u, -d]:
            next = cur + i
            if 1 <= next <= f and not visited[next]:
                visited[next] = 1
                count[next] = count[cur] + 1
                q.append(next)
        

f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)
count = [0] * (f + 1)
bfs()
print("use the stairs")