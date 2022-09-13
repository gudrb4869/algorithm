def solution(s):
    tuples = sorted([set(map(int, c.split(','))) for c in s[2:-2].split('},{')])
    answer = []
    for t in tuples:
        for e in t:
            if e not in answer:
                answer.append(e)
    return answer