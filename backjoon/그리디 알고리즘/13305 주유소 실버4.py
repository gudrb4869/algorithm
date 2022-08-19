import sys
input = sys.stdin.readline
n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
answer, cur = 0, cost[0]
for i in range(n - 1):
    cur = min(cur, cost[i])
    answer += cur * dist[i]
print(answer)