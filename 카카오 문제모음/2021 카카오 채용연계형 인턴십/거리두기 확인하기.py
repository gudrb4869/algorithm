dr, dc = (1,0,-1,0),(0,1,0,-1)

def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        return 0
            elif place[r][c] == 'O':
                count = 0
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        count += 1
                if count >= 2:
                    return 0
    return 1
                    
def solution(places):
    result = []
    for place in places:
        result.append(check(place))
    return result