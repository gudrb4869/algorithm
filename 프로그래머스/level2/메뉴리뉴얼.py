from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        lst = []
        for order in orders:
            for l in list(combinations(sorted(order), c)):
                lst.append(''.join(l))
        result = Counter(lst).most_common()
        if result and result[0][1] > 1:
            maximum = result[0][1]
            for r in result:
                if r[1] == maximum:
                    answer.append(r[0])
    answer.sort()
    return answer