class Solution:
    def twosum(self, nums : list[int], target : int) -> list[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

if __name__ == '__main__':
    solution = Solution()
    print(solution.twosum(list(map(int, input().split())), int(input())))