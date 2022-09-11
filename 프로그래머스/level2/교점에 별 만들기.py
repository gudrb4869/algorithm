def solution(line):
    coor = set()
    n = len(line)
    for i in range(n):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]
            if a*d - b*c == 0:
                continue
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            if x == int(x) and y == int(y):
                coor.add((int(x), int(y)))
    xs = list(x for x, _ in list(coor))
    ys = list(y for _, y in list(coor))
    min_x, min_y, max_x, max_y = min(xs), min(ys), max(xs), max(ys)
    arr = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for x, y in coor:
        arr[y - min_y][x - min_x] = '*'
    return [''.join(a) for a in reversed(arr)]