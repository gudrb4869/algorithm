from typing import List
import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1'''

        '''for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v

            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left  = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1'''

        '''for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k + 1:], expected)
            if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2'''

        '''for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2'''

        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1