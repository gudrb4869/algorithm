import sys
input = sys.stdin.readline

def dfs(r, c, d):
    visited[r][c] = 1
    for i in range(1, 5):
        nd = (d - i) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if not visited[nr][nc] and not matrix[nr][nc]:
            dfs(nr, nc, nd)
    br = r - dr[d]
    bc = c - dc[d]
    if not matrix[br][bc]:
        dfs(br, bc, nd)
    print(sum(visit.count(1) for visit in visited))
    exit(0)
    
    
n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
dfs(r, c, d)