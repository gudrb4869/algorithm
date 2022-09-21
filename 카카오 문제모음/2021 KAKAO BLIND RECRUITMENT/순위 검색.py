from itertools import product
from bisect import bisect_left
from collections import defaultdict

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for i in info:
        i = i.split()
        point = int(i[4])
        for a,b,c,d in list(product((0, 1), repeat=4)):
            dic[('-' if a else i[0], '-' if b else i[1], '-' if c else i[2], '-' if d else i[3])].append(point)
    for key in dic.keys():
        dic[key].sort()
    for q in query:
        q = q.split()
        curr = (q[0], q[2], q[4], q[6])
        value = int(q[7])
        answer.append(len(dic[curr]) - bisect_left(dic[curr], value))
    return answer