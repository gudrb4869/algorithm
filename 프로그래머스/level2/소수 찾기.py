from itertools import permutations

def solution(numbers):
    def isPrime(n):
        if n <= 1: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    result = set()
    for i in range(1, len(numbers) + 1):
        perms = list(permutations(numbers, i))
        for perm in perms:
            num = int(''.join(perm))
            if isPrime(num):
                result.add(num)
                    
    return len(result)