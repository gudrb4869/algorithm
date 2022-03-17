def dfs(k, cnt):
    if k == y:
        print(cnt)
        exit(0)
    visit[k] = 1
    for i in graph[k]:
        if not visit[i]:
            dfs(i, cnt + 1)

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(m):
    graph[i].sort()

dfs(x, 0)
print(-1)