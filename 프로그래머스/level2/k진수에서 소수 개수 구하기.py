def solution(n, k):
    def convert(n, base):
        rev_base = ''
        while n > 0:
            n, mod = divmod(n, base)
            rev_base += str(mod)
            
        return rev_base[::-1]
        
    def isPrimeNumber(n):
        if n == 1:
            return False
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    answer = 0
    for num in convert(n, k).split('0'):
        if num and isPrimeNumber(int(num)):
            answer += 1
    
    return answer