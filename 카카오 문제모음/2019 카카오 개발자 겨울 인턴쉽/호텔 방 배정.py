'''
import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
table = defaultdict(int)

def find(x):
    if table[x] == 0:
        table[x] = x + 1
        return x
    else:
        table[x] = find(table[x])
        return table[x]
        
    
def solution(k, room_number):
    result = []
    for i in room_number:
        result.append(find(i))
    return result
'''
def solution(k, room_number):
    result = []
    dic = dict()
    for i in room_number:
        cur = i
        visit = [cur]
        while cur in dic:
            cur = dic[cur]
            visit.append(cur)
        result.append(cur)
        for j in visit:
            dic[j] = cur + 1
    return result