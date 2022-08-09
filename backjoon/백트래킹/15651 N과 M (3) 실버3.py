# from itertools import product
# n, m = map(int, input().split())
# nums = [i for i in range(1, n + 1)]
# for result in list(product(nums, repeat=m)):
#     print(*result)

def dfs(x):
    if x == m:
        for i in range(1, m + 1):
            print(nums[i], end=' ')
        print()
    else:
        for i in range(1, n + 1):
            nums[x + 1] = i
            dfs(x + 1)

n, m = map(int, input().split())
nums = [0] * 8
dfs(0)