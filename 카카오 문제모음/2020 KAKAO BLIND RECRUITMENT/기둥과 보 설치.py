def check(x, y, a, arr):
    if a == 0:
        if y == 0 or arr[x][y - 1][0] or arr[x - 1][y][1] or arr[x][y][1]:
            return True
    else:
        if arr[x][y - 1][0] or arr[x + 1][y - 1][0] or (arr[x - 1][y][1] and arr[x + 1][y][1]):
            return True
    return False

def solution(n, build_frame):
    result = []
    arr = [[[False] * 2 for _ in range(n + 1)] for _ in range(n + 1)]
    for x, y, a, b in build_frame:
        if b == 1:
            result.append([x, y, a])
            arr[x][y][a] = True
            for i, j, k in result:
                if not check(i, j, k, arr):
                    result.remove([x, y, a])
                    arr[x][y][a] = False
                    break
        else:
            result.remove([x, y, a])
            arr[x][y][a] = False
            for i, j, k in result:
                if not check(i, j, k, arr):
                    result.append([x, y, a])
                    arr[x][y][a] = True
                    break
            
    return sorted(result)