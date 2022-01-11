from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2

def printTree(root: TreeNode) -> None:
    queue = [root]
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                print(node.val, end= ' ')
            else:
                print('null', end = ' ')
        print()

solution = Solution()
root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
answer = solution.mergeTrees(root1, root2)
# printTree(root1)
# printTree(root2)
printTree(answer)