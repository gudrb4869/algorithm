n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
max_val, min_val = -int(1e9), int(1e9)
def dfs(x, val):
    global max_val, min_val
    if x == n - 1:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    for i in range(4):
        if op[i]:
            op[i] -= 1
            if i == 0:
                dfs(x + 1, val + num[x + 1])
            elif i == 1:
                dfs(x + 1, val - num[x + 1])
            elif i == 2:
                dfs(x + 1, val * num[x + 1])
            else:
                dfs(x + 1, int(val / num[x + 1]))
            op[i] += 1

dfs(0, num[0])
print(max_val)
print(min_val)