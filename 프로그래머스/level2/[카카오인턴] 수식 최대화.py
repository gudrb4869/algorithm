import re
from itertools import permutations

def solution(expression):
    answer = 0
    
    for operands in list(permutations(['*', '+', '-'], 3)):
        numbers = re.findall('[0-9]{1,3}', expression)
        ops = re.findall('[*+-]', expression)
        for op in operands:
            while op in ops:
                i = ops.index(op)
                numbers.insert(i, str(eval(numbers.pop(i) + ops.pop(i) + numbers.pop(i))))
        answer = max(answer, abs(int(numbers[0])))
    return answer