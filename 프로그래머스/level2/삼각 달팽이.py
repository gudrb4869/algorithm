def solution(n):
    arr = [[1] * i for i in range(1, n + 1)]
    cur, num = n, 0
    row, col = -1, 0
    while cur > 0:
        for _ in range(cur):
            row += 1
            num += 1
            arr[row][col] = num
        for _ in range(cur - 1):
            col += 1
            num += 1
            arr[row][col] = num
        for _ in range(cur - 2):
            row -= 1
            col -= 1
            num += 1
            arr[row][col] = num
        cur -= 3
    return sum(arr, [])