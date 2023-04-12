import sys
input = sys.stdin.readline
R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
ans = 0
def dfs(r, c):
    if c == C - 1:
        return True
    
    for d in (-1, 0, 1):
        nr = r + d
        nc = c + 1
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and arr[nr][nc] == '.':
                visited[nr][nc] = True
                arr[nr][nc] = 'x'
                if dfs(nr, nc):
                    return True
                arr[nr][nc] = '.'
    return False

for i in range(R):
    arr[i][0] = 'x'
    if dfs(i, 0):
        ans += 1
    arr[i][0] = '.'
print(ans)