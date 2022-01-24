'''dartResult = input()
result = []
dict = {'S': 1, 'D': 2, 'T': 3,}
for i, c in enumerate(dartResult):
    if c.isdigit() and dartResult[i+1] in dict:
        result.append(int(c) ** dict[dartResult[i+1]])
        if i+2 < len(dartResult) and dartResult[i+2] == '*':
            result[-1] *= 2
            if len(result) > 1:
                result[-2] *= 2
        elif i+2 < len(dartResult) and dartResult[i+2] == '#':
            result[-1] *= -1
print(sum(result))'''

dartResult = input()
nums = [0]
for s in dartResult:
    if s == 'S':
        nums[-1] **= 1
        nums.append(0)
    elif s == 'D':
        nums[-1] **= 2
        nums.append(0)
    elif s == 'T':
        nums[-1] **= 3
        nums.append(0)
    elif s == '*':
        nums[-2] *= 2
        if len(nums) > 2:
            nums[-3] *= 2
    elif s == '#':
        nums[-2] *= -1
    else:
        nums[-1] = nums[-1] * 10 + int(s)
print(nums)
print(sum(nums))