from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest

solution = Solution()
print(solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))