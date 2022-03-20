from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while queue:
        x, y, z, day = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<h and 0<=ny<n and 0<=nz<m and arr3[nx][ny][nz] == 0:
                    arr3[nx][ny][nz] = 1
                    queue.append((nx, ny, nz, day + 1))
    for arr2 in arr3:
        for arr in arr2:
            if 0 in arr:
                print(-1)
                exit(0)
    print(day)

m,n,h=map(int, input().split())
arr3 = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = (1,-1,0,0,0,0)
dy = (0,0,1,-1,0,0)
dz = (0,0,0,0,1,-1)
queue = deque()
for x in range(h):
    for y in range(n):
        for z in range(m):
            if arr3[x][y][z] == 1:
                queue.append((x, y, z, 0))
bfs()
