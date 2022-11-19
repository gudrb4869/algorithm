# import sys
# input = sys.stdin.readline

# def dfs(x):
#     global answer
#     visited[x] = True
#     for y in graph[x]:
#         if not visited[y]:
#             answer += 1
#             dfs(y)

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     graph = [[] for _ in range(n + 1)]
#     visited = [False] * (n + 1)
#     answer = 0
#     for _ in range(m):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     dfs(1)
#     print(answer)

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
    print(n - 1)