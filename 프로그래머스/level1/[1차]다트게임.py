def solution(dartResult):
    answer = 0
    lst = []
    val = ''
    
    for d in dartResult:
        if d >= '0' and d <= '9':
            val += d
            continue
        else:
            if val != '':
                lst.append(int(val))
                val = ''
                
        if d == 'D':
            lst[-1] **= 2
        elif d == 'T':
            lst[-1] **= 3
        elif d == '#':
            lst[-1] *= -1
        elif d == '*':
            lst[-1] *= 2
            if len(lst) > 1:
                lst[-2] *= 2
    
    return sum(lst)