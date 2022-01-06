from typing import List
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
                
        dfs(nums)
        return results
        '''

        return list(map(list, itertools.permutations(nums)))

solution = Solution()
print(solution.permute([1,2,3]))