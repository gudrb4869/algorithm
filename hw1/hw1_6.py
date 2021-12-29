import re
p = re.compile('^((100+1+|01)+)$')
result=[]
x = int(input())
for i in range(x):
    m = p.match(str(input()))
    if m != None:
        result.append('DANGER')
    else:
        result.append('PASS')
for i in range(x):
    print(result[i])