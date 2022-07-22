def solution(numbers):    
    return str(int(''.join(str(e) for e in sorted(numbers, key=lambda x : -int((str(x) * 4)[:4])))))
