def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2

def convert(n, k):
    result = ''
    while n:
        n, mod = divmod(n, k)
        result += str(mod)
    return result[::-1]

def solution(n, k):
    answer = 0
    for num in list(filter(None, convert(n, k).split('0'))):
        if isPrime(int(num)):
            answer += 1
    return answer