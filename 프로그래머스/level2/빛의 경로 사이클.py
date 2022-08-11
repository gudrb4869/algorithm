def solution(grid):
    di, dj = (-1,0,1,0), (0,1,0,-1)
    arr = [[[0, 0, 0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    answer = []
    m, n = len(arr), len(arr[0])
    def traverse(i, j, k):
        dist = 0
        while not arr[i][j][k]:
            arr[i][j][k] = 1
            dist += 1
            
            i = (i + di[k]) % m
            j = (j + dj[k]) % n
            
            if grid[i][j] == 'L':
                k = (k + 1) % 4
            elif grid[i][j] == 'R':
                k = (k - 1) % 4
                
        return dist

    for i in range(m):
        for j in range(n):
            for k in range(4):
                if not arr[i][j][k]:
                    answer.append(traverse(i, j, k))
    
    return sorted(answer)