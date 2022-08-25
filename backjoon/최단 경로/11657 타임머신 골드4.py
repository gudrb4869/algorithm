'''
간선의 가중치 중에서 음수 가중치가 존재하기 때문에
다익스트라 알고리즘 대신 벨만-포드 알고리즘을 사용했다.
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for cur, nxt, cost in edges:
            if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
                if i == n - 1:
                    return True
                dist[nxt] = dist[cur] + cost
    return False

if bellman_ford(1):
    print(-1)
else:
    for i in range(2, n + 1):
        print(-1 if dist[i] == INF else dist[i])