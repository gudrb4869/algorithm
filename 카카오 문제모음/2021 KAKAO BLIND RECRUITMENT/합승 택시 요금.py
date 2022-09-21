def solution(n, s, a, b, fares):
    INF = 10**9
    arr = [[INF] * (n + 1) for _ in range(n + 1)]
    for c, d, f in fares:
        arr[c][d] = f
        arr[d][c] = f
    
    for i in range(1, n + 1):
        arr[i][i] = 0
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
                
    return min(arr[s][i] + arr[i][a] + arr[i][b] for i in range(1, n + 1))