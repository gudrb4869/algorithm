from math import log

def check(x):
    if len(x) <= 1:
        return True
    mid = len(x) // 2
    if x[mid] == '1':
        return check(x[:mid]) and check(x[mid + 1:])
    else:
        return x.find('1') == -1
        
def solution(numbers):
    answer = []
    for x in numbers:
        if x == 1:
            answer.append(1)
        else:
            p = 2 ** (int(log(int(log(x) / log(2)) + 1) / log(2)) + 1) - 1
            num = bin(x)[2:].zfill(p)
            answer.append(1 if check(num) else 0)
    return answer