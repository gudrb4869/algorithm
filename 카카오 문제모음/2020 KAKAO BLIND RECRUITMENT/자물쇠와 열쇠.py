def rotate(arr):
    r, c = len(arr), len(arr[0])
    result = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            result[j][c - i - 1] = arr[i][j]
    return result

def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[m + i][m + j] != 1:
                return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    board = [[0] * (n + m * 2) for _ in range(n + m * 2)]
    for i in range(n):
        for j in range(n):
            board[m + i][m + j] = lock[i][j]

    for _ in range(4):
        for i in range(1, m + n):
            for j in range(1, m + n):
                for r in range(m):
                    for c in range(m):
                        board[i + r][j + c] += key[r][c]

                if check(board, m, n):
                    return True

                for r in range(m):
                    for c in range(m):
                        board[i + r][j + c] -= key[r][c]
        key = rotate(key)
    return False