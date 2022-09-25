for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + arr[i]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for diagonal in range(n - 1):
        for i in range(1, n - diagonal):
            j = i + diagonal + 1
            dp[i][j] = min([dp[i][k] + dp[k + 1][j] for k in range(i, j)]) + (s[j] - s[i - 1])
    print(dp[1][n])