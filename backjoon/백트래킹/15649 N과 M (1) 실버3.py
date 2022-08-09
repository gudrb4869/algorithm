# from itertools import permutations
# n, m = map(int, input().split())
# nums = [i for i in range(1, n + 1)]
# for result in list(permutations(nums, m)):
#     print(*result)

def promising(x):
    for i in range(1, x):
        if nums[i] == nums[x]:
            return False
    return True

def dfs(x):
    if promising(x):
        if x == m:
            for i in range(1, m + 1):
                print(nums[i], end=' ')
            print()
        else:
            for i in range(1, n + 1):
                nums[x + 1] = i
                dfs(x + 1)


n, m = map(int, input().split())
nums = [0] * 9
dfs(0)
