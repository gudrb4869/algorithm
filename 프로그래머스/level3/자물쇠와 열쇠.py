def rotate(arr, d):
    n = len(arr)
    result = [[0] * n for _ in range(n)]
    if d % 4 == 1:
        for r in range(n):
            for c in range(n):
                result[c][n-1-r] = arr[r][c]
    elif d % 4 == 2:
        for r in range(n):
            for c in range(n):
                result[n-1-r][n-1-c] = arr[r][c]
    elif d % 4 == 3:
        for r in range(n):
            for c in range(n):
                result[n-1-c][r] = arr[r][c]
    else:
        for r in range(n):
            for c in range(n):
                result[r][c] = arr[r][c]
                
    return result

def check(board, M, N):
    for r in range(N):
        for c in range(N):
            if board[M + r][M + c] != 1:
                return False
    return True
            
def solution(key, lock):
    M, N = len(key), len(lock)
    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    for r in range(N):
        for c in range(N):
            board[M + r][M + c] = lock[r][c]
            
    for i in range(1, M + N):
        for j in range(1, M + N):
            for d in range(4):
                rotated_key = rotate(key, d)
                                
                for r in range(M):
                    for c in range(M):
                        board[i + r][j + c] += rotated_key[r][c]
                
                if check(board, M, N):
                    return True
                
                for r in range(M):
                    for c in range(M):
                        board[i + r][j + c] -= rotated_key[r][c]
    
    return False