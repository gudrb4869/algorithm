from collections import defaultdict
n = int(input())
tree = defaultdict(list)
for _ in range(n):
    p, l, r = input().split()
    tree[p].append(l)
    tree[p].append(r)

def preorder(cur):
    if cur != '.':
        print(cur, end='')
        preorder(tree[cur][0])
        preorder(tree[cur][1])
def inorder(cur):
    if cur != '.':
        inorder(tree[cur][0])
        print(cur, end='')
        inorder(tree[cur][1])
def postorder(cur):
    if cur != '.':
        postorder(tree[cur][0])
        postorder(tree[cur][1])
        print(cur, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')