from typing import List
import collections

class Solution:
    def add_to_deque(self, dq, nums, i):
        while len(dq) and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)

        result, start, end = [], 0, k - 1

        while len(nums) > end:
            while True:
                if len(dq) and dq[0] >= start:
                    result.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()

            start, end = start + 1, end + 1

            if len(nums) > end:
                while dq and nums[dq[-1]] <= nums[end]:
                    dq.pop()
                dq.append(end)

        return result
        '''if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))

        return r'''

        '''results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
        return results'''