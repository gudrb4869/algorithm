import re
from itertools import permutations

def solution(expression):
    answer = 0
    for operands in list(permutations(['*', '+', '-'], 3)):
        nums = re.findall('\d{1,3}', expression)
        ops = re.findall('[*+-]', expression)
        for op in operands:
            while op in ops:
                i = ops.index(op)
                nums.insert(i, str(eval(nums.pop(i) + ops.pop(i) + nums.pop(i))))
        answer = max(answer, abs(int(nums[0])))
    return answer