def solution(board, skill):
    n, m = len(board), len(board[0])
    arr = [[0] * (m + 1) for _ in range(n + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        arr[r1][c1] += -degree if t == 1 else degree
        arr[r1][c2 + 1] += degree if t == 1 else -degree
        arr[r2 + 1][c1] += degree if t == 1 else -degree
        arr[r2 + 1][c2 + 1] += -degree if t == 1 else degree

    answer = 0
    for i in range(n):
        for j in range(1, m + 1):
            arr[i][j] += arr[i][j - 1]
    for i in range(1, n + 1):
        for j in range(m):
            arr[i][j] += arr[i - 1][j]
    for i in range(n):
        for j in range(m):
            if board[i][j] + arr[i][j] > 0:
                answer += 1
    return answer