from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for perm in list(permutations(dungeons)):
        cur, cnt = k, 0
        for require, consume in perm:
            if cur >= require:
                cnt += 1
                cur -= consume
        answer = max(answer, cnt)
                
    return answer