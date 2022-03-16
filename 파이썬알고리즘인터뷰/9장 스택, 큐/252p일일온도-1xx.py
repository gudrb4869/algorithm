from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)
        return result

solution=Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))