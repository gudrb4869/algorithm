from typing import List

def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    sum = 0
    for i, v in enumerate(nums):
        if i % 2 == 0:
            sum += v

    return sum
        

print(arrayPairSum([1,4,3,2]))