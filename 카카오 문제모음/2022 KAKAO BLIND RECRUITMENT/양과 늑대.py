from collections import defaultdict
        
def solution(info, edges):
    def search(lst, s, w):
        if s <= w or not lst:
            return s
        result = 1
        for i, cur in enumerate(lst):
            result = max(result, search(lst[:i] + tree[cur] + lst[i + 1:], s if info[cur] else s + 1, w + 1 if info[cur] else w))
        return result
        
    tree = defaultdict(list)
    for p, c in edges:
        tree[p].append(c)
    return search(tree[0], 1, 0)