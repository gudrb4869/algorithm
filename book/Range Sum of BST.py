from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue, sum = collections.deque([root]), 0

        while queue:
            node = queue.popleft()
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum
        
        '''
        stack, sum = [root], 0

        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum
        '''
        
        '''
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
        '''

        '''
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) + \
            self.rangeSumBST(root.left, low, high) + \
            self.rangeSumBST(root.right, low, high)
        '''

        '''
    # 내가 짠 코드
    sum: int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        
        if root.val < low:
            self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            self.rangeSumBST(root.left, low, high)
        else:
            self.sum += root.val
            self.rangeSumBST(root.left, low, root.val)
            self.rangeSumBST(root.right, root.val + 1, high)

        return self.sum
        # '''
