from itertools import combinations

def solution(numbers):
    answer = []
    combs = list(combinations(numbers, 2))
    for comb in combs:
        if sum(comb) not in answer:
            answer.append(sum(comb))
    answer.sort()
    return answer