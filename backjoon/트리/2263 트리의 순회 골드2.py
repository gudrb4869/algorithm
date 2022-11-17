import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 메모리 초과
# def dfs(inorder, postorder):
#     if inorder and postorder:
#         idx = inorder.index(postorder[-1])
#         print(inorder[idx], end=' ')
#         dfs(inorder[:idx], postorder[:idx])
#         dfs(inorder[idx+1:], postorder[idx:-1])
# dfs(inorder, postorder)

# 시간 초과
# def dfs(l1, h1, l2, h2):
#     if l1 <= h1 and l2 <= h2:
#         mid = inorder.index(postorder[h2])
#         print(inorder[mid], end=' ')
#         dfs(l1, mid - 1, l2, mid - 1 - (h1 - h2))
#         dfs(mid + 1, h1, mid - (l1 - l2), h2 - 1)
    
# dfs(0, n - 1, 0, n - 1)

position = {inorder[i]: i for i in range(n)}
def dfs(l1, h1, l2, h2):
    if l1 <= h1 and l2 <= h2:
        root = postorder[h2]
        mid = position[root]
        print(root, end=' ')
        dfs(l1, mid - 1, l2, mid - 1 - (h1 - h2))
        dfs(mid + 1, h1, mid - (l1 - l2), h2 - 1)
    
dfs(0, n - 1, 0, n - 1)