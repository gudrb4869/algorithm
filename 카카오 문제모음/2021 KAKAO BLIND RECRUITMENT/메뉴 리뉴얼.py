from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    for c in course:
        cand = []
        for order in orders:
            cand += list(combinations(sorted(order), c))
        cand = sorted(Counter(cand).items(), key=lambda x: -x[1])
        if cand:
            maximum = cand[0][1]
            while maximum > 1 and cand and cand[0][1] == maximum:
                result.append(''.join(cand.pop(0)[0]))
    return sorted(result)