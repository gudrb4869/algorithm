import collections, sys
input = sys.stdin.readline
n = int(input())
k = int(input())

dict = collections.defaultdict(set)
visited = [False] * (100 + 1)

for _ in range(k):
    i, j = map(int, input().split())
    dict[i].add(j)
    dict[j].add(i)

queue = collections.deque()
queue.append(1)
# visited[1] = True
# while queue:
#     i = queue.popleft()
#     if visited[i]:
#         for j in dict[i]:
#             if not visited[j]:
#                 visited[j] = True
#                 queue.append(j)
def dfs(x):
    visited[x] = True
    for i in dict[x]:
        if not visited[i]:
            dfs(i)
    
dfs(1)
print(visited.count(True) - 1)
