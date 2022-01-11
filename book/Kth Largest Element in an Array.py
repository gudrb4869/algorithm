from typing import List
import collections, heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Most Frequent
        # freqs = collections.Counter(nums)
        # freqs_heap = list()
        # for f in freqs:
        #     heapq.heappush(freqs_heap, (-freqs[f], f))

        # topk = list()
        # for _ in range(1, k):
        #     topk.append(heapq.heappop(freqs_heap[1]))

        # return topk

        # Largest (Use a heap module)
        '''heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)'''

        # use heapify of heap module
        '''heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)'''
        
        '''return heapq.nlargest(k, nums)[-1]'''

        return sorted(nums, reverse=True)[k - 1]