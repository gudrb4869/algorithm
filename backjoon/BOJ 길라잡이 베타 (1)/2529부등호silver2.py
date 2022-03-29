k = int(input())
op = list(map(str, input().split()))
visit = [0] * 10
mx, mn = '', ''
def dfs(idx, s):
    global mx, mn
    if idx == k + 1:
        if mn == '':
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if not visit[i]:
            if idx == 0 or eval(s[-1] + op[idx - 1] + str(i)):
                visit[i] = 1
                dfs(idx + 1, s + str(i))
                visit[i] = 0
dfs(0, '')
print(mx)
print(mn)