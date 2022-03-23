import sys
input = sys.stdin.readline
s1 = list(input().strip())
s2 = []
cur = len(s1)

for _ in range(int(input())):
    a = input().split()
    if a[0] == 'P':
        s1.append(a[1])
        cur += 1
    elif a[0] == 'L' and s1 != []:
        s2.append(s1.pop())
    elif a[0] == 'D' and s2 != []:
        s1.append(s2.pop())
    elif a[0] == 'B' and s1 != []:
        s1.pop()

print("".join(s1 + list(reversed(s2))))