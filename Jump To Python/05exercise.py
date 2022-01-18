
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
# 1
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
# 2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if(self.value > 100): self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# 3
all([1, 2, abs(-3)-3]) # False
chr(ord('a')) == 'a' # True

# 4 잘모르겟음
# lst = [1, -2, 3, -5, 8, 3]
# # lst = list(filter(lambda a: a if a>=0 else None, lst))
# print(lst)
print(list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3])))

# 5
print(int('0xea', 16))

# 6 잘 모르겟음
# lst = [1,2,3,4]
# print(map(lambda a: a*3 for a in lst,[1,2,3,4]))
print(list(map(lambda x:x*3, [1,2,3,4])))
# 7
lst = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(lst) + min(lst))

# 8
print(round(17 / 3, 4))

# 9 myargv.py
import sys
sum = 0
for i in sys.argv[1:]:
    sum += int(i)
print(sum)

# 10
import os
os.chdir("C:/doit")
result = os.popen("dir")
print(result.read())

# 11 잘 모르겟음
import glob
print(glob.glob("C:/doit/*.py"))

# 12
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# 13 잘 모르겟음
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)