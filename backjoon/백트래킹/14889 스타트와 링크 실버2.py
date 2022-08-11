# from itertools import combinations
# n = int(input())
# s = [list(map(int, input().split())) for _ in range(n)]
# nums = {i for i in range(n)}
# result = []
# for start_team in combinations(nums, n // 2):
#     link_team = nums - set(start_team)
#     start, link = 0, 0
#     for i, j in list(combinations(start_team, 2)):
#         start += s[i][j] + s[j][i]
#     for i, j in list(combinations(link_team, 2)):
#         link += s[i][j] + s[j][i]
#     result.append(abs(start - link))

# print(min(result))

from itertools import combinations
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
start_team, link_team = [], []
result = []
def dfs(x):
    if x == n:
        if len(start_team) == n // 2 and len(link_team) == n // 2:
            start, link = 0, 0
            for i, j in combinations(start_team, 2):
                start += s[i][j] + s[j][i]
            for i, j in combinations(link_team, 2):
                link += s[i][j] + s[j][i]
            result.append(abs(start - link))
        return
    
    start_team.append(x)
    dfs(x + 1)
    start_team.pop()
    link_team.append(x)
    dfs(x + 1)
    link_team.pop()

dfs(0)
print(min(result))