from collections import deque

N,M,T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]
visit = [[[False] * 2 for _ in range(M)] for _ in range(N)]
visit[0][0][0] = True
queue = deque()
queue.append([0,0,0,0])

def bfs():
    while queue:
        q = queue.popleft()
        r, c, t, weapon = q[0], q[1], q[2], q[3]

        if t > T:
            print("Fail")
            return

        if r == N-1 and c == M-1:
            print(str(t))
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            nt = t + 1
            if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc][weapon]:
                if weapon == 1:
                    visit[nr][nc][weapon] = True
                    queue.append([nr, nc, nt, 1])
                else:
                    if lst[nr][nc] == 0:
                        visit[nr][nc][weapon] = True
                        queue.append([nr, nc, nt, 0])
                    elif lst[nr][nc] == 2:
                        visit[nr][nc][weapon] = True
                        queue.append([nr, nc, nt, 1])
    print("Fail")
    return
bfs()