import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data: str) -> TreeNode:
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
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
                print('#', end = ' ')
        print()

# Your Codec object will be instantiated and called as such:
null = -1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
ser = Codec()
deser = Codec()
print(ser.serialize(root))
ans = deser.deserialize(ser.serialize(root))
printTree(ans)