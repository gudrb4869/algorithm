from itertools import permutations

def solution(n, weak, dist):
    W, D = len(weak), len(dist)
    answer = D + 1
    perms = list(permutations(dist))
    for _ in range(W):
        for perm in perms:
            result = 1
            cur = weak[0] + perm[0]
            for i in range(W):
                if weak[i] > cur:
                    result += 1
                    if result > D:
                        break
                    cur = weak[i] + perm[result - 1]
            
            if result <= D:
                answer = min(answer, result)
                
        weak.append(weak.pop(0) + n)
    
    return -1 if answer > D else answer