from collections import defaultdict

def solution(gems):
    n = len(gems)
    cnt = len(set(gems))
    answer = [1, n]
    dic = defaultdict(int)
    right = 0
    for left, gem in enumerate(gems):
        while len(dic) < cnt and right < n:
            dic[gems[right]] += 1
            right += 1
        if len(dic) == cnt and right - left < answer[1] - answer[0] + 1:
            answer = [left + 1, right]
        dic[gem] -= 1
        if dic[gem] == 0:
            del(dic[gem])
    return answer