import collections
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
queue = collections.deque()
queue.append((0, 0, 1))
visited[0][0] = True
while queue:
    r, c, cnt = queue.popleft()
    if r == n - 1 and c == m - 1:
        print(cnt)
        exit(0)
    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]
        if 0 <= new_r < n and 0 <= new_c < m:
            if not visited[new_r][new_c] and graph[new_r][new_c] == '1':
                visited[new_r][new_c] = True
                queue.append((new_r, new_c, cnt + 1))