from typing import List
import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        Q = [(0, k)]
        dist = collections.defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == n:
            return max(dist.values())
        return -1

solution = Solution()
times, N, K = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
# times, N, K = [[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]], 8, 3
print(solution.networkDelayTime(times, N, K))