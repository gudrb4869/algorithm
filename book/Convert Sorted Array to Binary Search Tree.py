from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

def printTree(root: TreeNode):
    queue = [root]
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
        
            if node:
                queue.append(node.left)
                queue.append(node.right)
                print(node.val, end= ' ')
            else:
                print('#', end = ' ')
        print()

solution = Solution()
nums = [-10,-7,-3,0,5,7,9]
ans = solution.sortedArrayToBST(nums)
printTree(ans)