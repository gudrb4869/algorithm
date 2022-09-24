from collections import deque
INF = 10 ** 3
n, m = map(int, input().split())
board = [i for i in range(101)]
dist = [INF for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y

for m in range(m):
    u, v = map(int, input().split())
    board[u] = v

q = deque()
q.append(1)
dist[1] = 0
def bfs():
    while q:
        x = q.popleft()
        if x == 100:
            return dist[100]
        for i in range(1, 7):
            nx = x + i
            if nx <= 100 and dist[board[x]] + 1 < dist[board[nx]]:
                dist[board[nx]] = dist[board[x]] + 1
                q.append(board[nx])

print(bfs())