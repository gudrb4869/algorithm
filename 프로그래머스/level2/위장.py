from collections import Counter
from functools import reduce

def solution(clothes):
    return reduce(lambda x, y : x * y, [a+1 for a in Counter(c[1] for c in clothes).values()]) - 1