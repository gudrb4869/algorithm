import sys
input = sys.stdin.readline
a, result = [], 0
for _ in range(int(input())):
    a.append(int(input()))
a.sort(reverse=True)
while a:
    result = max(result, a.pop() * (len(a) + 1))
print(result)