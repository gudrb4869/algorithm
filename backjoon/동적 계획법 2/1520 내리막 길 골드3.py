import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

def dfs(r, c):
    if (r, c) == (n - 1, m - 1):
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] < arr[r][c]:
            dp[r][c] += dfs(nr, nc)
    return dp[r][c]

print(dfs(0, 0))