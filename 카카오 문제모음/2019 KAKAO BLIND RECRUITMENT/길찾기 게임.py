import sys
sys.setrecursionlimit(10**4)

def solution(nodeinfo):
    def make_tree(node):
        if not node:
            return None
        idx = node.index(max(node, key=lambda x: x[1]))
        tree[node[idx][2]] = [make_tree(node[:idx]), make_tree(node[idx+1:])]
        return node[idx][2]

    def preorder(node):
        if not node:
            return []
        return [node] + preorder(tree[node][0]) + preorder(tree[node][1])
    
    def postorder(node):
        if not node:
            return []
        return postorder(tree[node][0]) + postorder(tree[node][1]) + [node]
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort()
    tree = {}
    root = make_tree(nodeinfo)
    return [preorder(root), postorder(root)]