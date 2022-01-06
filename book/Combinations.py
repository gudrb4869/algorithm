from typing import List
import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(map(list, itertools.combinations(range(1, n + 1), k)))
        results = []
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        dfs([], 1, k)
        return results
        
solution = Solution()
print(solution.combine(4, 2))