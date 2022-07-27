from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    matrix = [[False] * 102 for _ in range(102)]
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                matrix[i][j] = True
                
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2 + 1, x2 * 2):
            for j in range(y1 * 2 + 1, y2 * 2):
                matrix[i][j] = False
                
    q = deque([(characterX * 2, characterY * 2, 0)])
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    matrix[characterX * 2][characterY * 2] = False
    
    while q:
        x, y, count = q.popleft()
        if (x, y) == (itemX * 2, itemY * 2):
            return count // 2
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny]:
                matrix[nx][ny] = False
                q.append((nx, ny, count + 1))