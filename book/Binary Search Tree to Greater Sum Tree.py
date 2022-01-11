from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        
        return root

def convertResult(root: TreeNode) -> List[int]:
    queue = [root]
    result = []
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
        
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(node.val)
    return result

solution = Solution()
root = solution.bstToGst(TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8)))))
print(convertResult(root))