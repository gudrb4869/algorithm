from itertools import permutations

def check(weak, dist):
    i = 0
    for d in dist:
        length = weak[i] + d
        while weak[i] <= length:
            i += 1
            if i == len(weak):
                return True
    return False

def solution(n, weak, dist):
    lw = len(weak)
    weak += [w + n for w in weak]
    weak = min([weak[i:i+lw] for i in range(lw)], key=lambda x: (x[-1] - x[0]))
    
    for i in range(1, len(dist) + 1):
        for d in list(permutations(dist, i)):
            if check(weak, d):
                return i
    return -1