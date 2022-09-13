from itertools import permutations

def check(users, banned_id):
    for i in range(len(users)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] != '*' and banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = 0
    l = []
    for users in list(permutations(user_id, len(banned_id))):
        if check(users, banned_id):
            s = set(users)
            if s not in l:
                l.append(s)
                answer += 1                
    return answer