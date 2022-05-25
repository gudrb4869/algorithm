def solution(places):
    answer = []
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    for place in places:
        flag = 1
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'O':
                    count = 0
                    for k in range(4):
                        new_r = r + dr[k]
                        new_c = c + dc[k]
                        if 0 <= new_r < 5 and 0 <= new_c < 5:
                            if place[new_r][new_c] == 'P':
                                count += 1
                    if count >= 2:
                        flag = 0
                elif place[r][c] == 'P':
                    for k in range(4):
                        new_r = r + dr[k]
                        new_c = c + dc[k]
                        if 0 <= new_r < 5 and 0 <= new_c < 5:
                            if place[new_r][new_c] == 'P':
                                flag = 0
                                break
                        
        answer.append(flag)
    return answer