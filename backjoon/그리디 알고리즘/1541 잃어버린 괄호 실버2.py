import re
s = '+' + input()
answer, flag = 0, False
for num, op in zip(re.findall(r'\d{1,5}', s), re.findall('[-|+]', s)):
    num = int(num)
    if op == '-':
        flag = True
    answer += -num if flag else num
print(answer)