from collections import defaultdict

def solution(gems):
    n, kind = len(gems), len(set(gems))
    result = [1, n]
    dic = defaultdict(int)
    dic[gems[0]] += 1
    
    left, right = 0, 0
    while left < n and right < n:
        if len(dic) < kind:
            right += 1
            if right == n: break
            dic[gems[right]] += 1
        else:
            if right - left < result[1] - result[0]:
                result = [left + 1, right + 1]
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1
    
    return result