from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True
    
    
def solution(user_id, banned_id):
    user_id = list(permutations(user_id, len(banned_id)))
    lst = []
        
    for users in user_id:
        if check(users, banned_id):
            users = set(users)
            if users not in lst:
                lst.append(users)
    
    return len(lst)