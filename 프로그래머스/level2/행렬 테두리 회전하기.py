def solution(rows, columns, queries):
    answer = []
    arr = [[i * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    for x1, y1, x2, y2 in queries:
        rmin, rmax = x1 - 1, x2 - 1
        cmin, cmax = y1 - 1, y2 - 1
        
        prev = arr[rmin + 1][cmin]
        result = prev
        
        for i in range(cmin, cmax):
            cur = arr[rmin][i]
            result = min(result, cur)
            arr[rmin][i] = prev
            prev = cur
        
        for i in range(rmin, rmax):
            cur = arr[i][cmax]
            result = min(result, cur)
            arr[i][cmax] = prev
            prev = cur
            
        for i in range(cmax, cmin, -1):
            cur = arr[rmax][i]
            result = min(result, cur)
            arr[rmax][i] = prev
            prev = cur
        
        for i in range(rmax, rmin, -1):
            cur = arr[i][cmin]
            result = min(result, cur)
            arr[i][cmin] = prev
            prev = cur
    
        answer.append(result)
    return answer