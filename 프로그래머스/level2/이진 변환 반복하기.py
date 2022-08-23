def solution(s):
    idx, count = 0, 0
    while s != '1':
        count += s.count('0')
        s = str(bin(s.count('1'))[2:])
        idx += 1
            
    return [idx, count]