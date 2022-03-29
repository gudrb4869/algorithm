n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

def dfs(idx, sum):
    global count
    if idx >= n:
        return

    sum += arr[idx]
    
    if sum == s:
        count += 1

    dfs(idx + 1, sum)
    dfs(idx + 1, sum - arr[idx])

dfs(0, 0)
print(count)