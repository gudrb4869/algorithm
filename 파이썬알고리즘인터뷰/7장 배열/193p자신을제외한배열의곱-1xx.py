from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1
    for i in range(len(nums)):
        out.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] *= p
        p *= nums[i]
    return out

print(productExceptSelf([1,2,3,4]))