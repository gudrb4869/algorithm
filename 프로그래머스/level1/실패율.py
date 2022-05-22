from collections import Counter
from collections import defaultdict

def solution(N, stages):
    answer = {}
    result = defaultdict(int)
    for l in list(Counter(stages).items()):
        result[l[0]] = l[1]
    total = len(stages)
    for i in range(1, N+1):
        answer[i] = 0 if total == 0 else result[i] / total
        total -= result[i]
    return sorted(answer, key=lambda x:(-answer[x], x))