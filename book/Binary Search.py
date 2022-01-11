from typing import List
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1'''
        '''def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)'''
        '''index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1'''
        try:
            return nums.index(target)
        except ValueError:
            return -1

        
solution = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(solution.search(nums, target))