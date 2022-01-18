# 06-1
'''def GuGu(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return result

result = GuGu(2)
print(result)
'''
# 06-2
'''sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)'''
# 06-3
'''from math import *
def getTotalPage(m, n):
    return ceil(m / n)

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))'''
#06-4
'''import sys
option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)'''
# 06-5
'''import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()'''
#06-6
def search(dirname):
    print(dirname)