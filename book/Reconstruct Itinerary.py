from typing import List
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            
        dfs('JFK')
        return route[::-1]
        '''

        '''
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
            
        dfs('JFK')
        return route[::-1]
        '''

        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]

solution = Solution()
lst1 = [
    ["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]
]
lst2 = [
    ["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]
]
lst3 = [
    ["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]
]
print(solution.findItinerary(lst3))