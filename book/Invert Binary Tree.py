from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left

        return root
        
        '''
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root
        '''

        '''
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root
        '''

        '''
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None
        '''

solution = Solution()
answer = solution.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))))

queue = [answer]
while queue:
    for _ in range(len(queue)):
        cur = queue.pop(0)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
        print(cur.val, end = ' ')
    print()
    