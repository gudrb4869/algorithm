# 1
'''str = "a:b:c:d"
print("#".join(str.split(":")))'''

# 2
a = {'A':90, 'B':80}
print(a.get('C', 70))
# 3
# a = [1,2,3]
# a += [4,5]
# print(a)
# a.extend([4,5])
# print(a)
# +를 사용하면 두 리스트가 더해진 새로운 리스트가 반환됨
# extend 사용시 주소 값이 변하지 않고 그대로 유지됨

# 4
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for x in A:
    if x >= 50:
        sum += x

print(sum)

# 5
import collections
dp = collections.defaultdict(int)
def fib(n):
    if n <= 1:
        return n
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# print(fib(int(input())))

# 6
'''nums = input().split(',')
sum = 0
for num in nums:
    sum += int(num)
print(sum)
'''
# 7   
# a = int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))
'''for i in range(1, 10):
    print(a * i, end=' ')
'''
# 8 잘 모르겟다
f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()
f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

# 9 잘 모르겟다
f = open("sample.txt", "r")
lines = f.readlines()
f.close()

sum = 0
for line in lines:
    sum += int(line)
avg = sum / len(lines)
f = open("result.txt", 'w')
f.write(str(avg))
f.close()

# 10
class Calculator:
    def __init__(self, numList):
        self.numList = numList

    def sum(self):
        sum = 0
        for num in self.numList:
            sum += num
        return sum

    def avg(self):
        return self.sum() / len(self.numList)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

# 11 잘 모르겟다
# import sys
# sys.path.append("c:/doit")
# import mymod

# 12 3 출력
# 답 7출력이다.

# 13 잘 모르겟다
data = "4546793"
numbers = list(map(int, data))
result = []
for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:
        is_odd = num % 2 == 1
        is_next_odd = numbers[i+1] % 2 == 1
        if is_odd and is_next_odd:
            result.append("-")
        elif not is_odd and not is_next_odd:
            result.append("*")

print("".join(result))

# 14 잘 모르겟다
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt: result += str(cnt)
    return result

print(compress_string("aaabbcccccca"))

# 15
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chkDupNum("0123456789"))
print(chkDupNum("01234"))
print(chkDupNum("01234567890"))
print(chkDupNum("6789012345"))
print(chkDupNum("012322456789"))


# 16
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}
def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))
# 17 2번과 매치

# 18 결괏값 = 10

# 19 잘 모르겟다
s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
import re
pat = re.compile('(\d{3}[-]\d{4})[-]\d{4}')
result = pat.sub('\g<1>-####', s)

print(result)
# 20
import re
pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))