class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BinaryTree:
    def __init__(self): 
        self.root = None

    def preorder(self,node):
        if node:
            print(node.val)
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)
    
    def inorder(self,node):
        if node:
            if node.left:
                self.inorder(node.left)
            print(node.val)
            if node.right:
                self.inorder(node.right)

    def postorder(self,node):
        if node:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print(node.val)

a=[Node(15),Node(1),Node(37),Node(61),Node(26),Node(59),Node(48)]
tree=BinaryTree()
tree.root=a[0]
a[0].left=a[1]
a[0].right=a[2]
a[1].left=a[3]
a[1].right=a[4]
a[2].left=a[5]
a[2].right=a[6]

print('Preorder Traverse')
tree.preorder(tree.root)
print('Inorder Traverse')
tree.inorder(tree.root)
print('Postorder Traverse')
tree.postorder(tree.root)