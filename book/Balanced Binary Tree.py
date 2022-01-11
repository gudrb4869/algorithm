from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    result: bool = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.result = False
            return max(left, right) + 1
        dfs(root)
        return self.result
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1

solution = Solution()
print(solution.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(solution.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))