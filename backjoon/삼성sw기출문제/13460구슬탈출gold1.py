import collections

n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]
Rr, Rc, Br, Bc = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'R':
            Rr, Rc = i, j
        if lst[i][j] == 'B':
            Br, Bc = i, j
dr = [-1,1,0,0] # 상,하,좌,우
dc = [0,0,-1,1] # 상,하,좌,우
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def go(r, c, dr, dc):
    count = 0
    while lst[r + dr][c + dc] != '#' and lst[r][c] != 'O':
        r += dr
        c += dc
        count += 1
    return r, c, count

def bfs(Rr, Rc, Br, Bc):
    q = collections.deque()
    q.append((Rr, Rc, Br, Bc, 1))
    while q:
        Rr, Rc, Br, Bc, res = q.popleft()
        visited[Rr][Rc][Br][Bc] = True
        if res > 10:
            print(-1)
            exit(0)
        for i in range(4):
            new_Rr, new_Rc, Rcount = go(Rr, Rc, dr[i], dc[i])
            new_Br, new_Bc, Bcount = go(Br, Bc, dr[i], dc[i])
                
            if lst[new_Br][new_Bc] != 'O':
                if lst[new_Rr][new_Rc] == 'O':
                    print(res)
                    exit(0)

                if new_Rr == new_Br and new_Rc == new_Bc:
                    if Rcount > Bcount:
                        new_Rr -= dr[i]
                        new_Rc -= dc[i]
                    else:
                        new_Br -= dr[i]
                        new_Bc -= dc[i]
                
                if not visited[new_Rr][new_Rc][new_Br][new_Bc]:
                    visited[new_Rr][new_Rc][new_Br][new_Bc] = True
                    q.append((new_Rr, new_Rc, new_Br, new_Bc, res + 1))
    print(-1)
    return

bfs(Rr, Rc, Br, Bc)