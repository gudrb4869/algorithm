def solution(n, results):
    answer = 0
    matrix = [[0] * n for _ in range(n)]
    for win, lose in results:
        matrix[win - 1][lose - 1] = 1
        matrix[lose - 1][win - 1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] == matrix[k][j] == 1:
                    matrix[i][j] = 1
                elif matrix[i][k] == matrix[k][j] == -1:
                    matrix[i][j] = -1
    
    for m in matrix:
        if m.count(0) == 1:
            answer += 1
    return answer