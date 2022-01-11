from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node
def printTree(root):
    queue = [root]
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node:
                print(node.val, end=' ')
                queue.append(node.left)
                queue.append(node.right)
            else:
                print('#', end=' ')
        print()
        
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

solution = Solution()
ans = solution.buildTree(preorder, inorder)
printTree(ans)

