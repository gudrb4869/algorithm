from itertools import combinations

def solution(relation):
    r, c = len(relation), len(relation[0])
    num = set()
    answer = []
    for k in range(c):
        for comb in list(combinations([k for k in range(c)], k + 1)):
            s = set()
            for i in range(r):
                l = []
                for j in comb:
                    l.append(relation[i][j])
                s.add(tuple(l))
            if len(s) == r:
                flag = 1
                for x in range(len(comb)):
                    for t in list(combinations(comb, x)):
                        if t in answer:
                            flag = 0
                            break
                if flag:
                    answer.append(comb)
    return len(answer)