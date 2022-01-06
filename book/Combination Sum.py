from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(csum, index, path):
            if csum == 0:
                results.append(path)
                return
            elif csum < 0:
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return results

solution = Solution()
print(solution.combinationSum([2,3,5],8))