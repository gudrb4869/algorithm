import sys

def solution(nodeinfo):
    def init(node):
        if not node:
            return None
        
        idx = node.index(max(node, key=lambda x: x[1]))
        tree[dic[tuple(node[idx])]] = [init(node[:idx]), init(node[idx + 1:])]
        return dic[tuple(node[idx])]
    
    def preorder(node):
        if node is None:
            return []
        return [node] + preorder(tree[node][0]) + preorder(tree[node][1])
    
    def postorder(node):
        if node is None:
            return []
        return postorder(tree[node][0]) + postorder(tree[node][1]) + [node]

    sys.setrecursionlimit(10**6)
    dic = {tuple(node) : i + 1 for i, node in enumerate(nodeinfo)}
    tree = {i + 1 : [None, None] for i in range(len(nodeinfo))}
    nodeinfo.sort(key=lambda x: (x[0], -x[1]))
    init(nodeinfo)
    root = dic[tuple(max(nodeinfo, key=lambda x: x[1]))]
    return [preorder(root), postorder(root)]