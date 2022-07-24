def solution(n, lost, reserve):
    arr = [1] * (n + 2)
    arr[0] = arr[n + 1] = 0
    for r in reserve:
        arr[r] += 1
    for l in lost:
        arr[l] -= 1
    for i in range(1, n + 1):
        if arr[i] == 0:
            if arr[i - 1] == 2:
                arr[i - 1] = arr[i] = 1
            elif arr[i + 1] == 2:
                arr[i] = arr[i + 1] = 1
    return arr.count(1) + arr.count(2)