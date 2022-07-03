from math import inf

def solution(n, s, a, b, fares):
    d = [[inf] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
        
    for i, j, cost in fares:
        d[i - 1][j - 1] = cost
        d[j - 1][i - 1] = cost
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    
    answer = d[s - 1][a - 1] + d[s - 1][b - 1]
    for k in range(n):
        answer = min(answer, d[s - 1][k - 1] + d[k - 1][a - 1] + d[k - 1][b - 1])
    return answer