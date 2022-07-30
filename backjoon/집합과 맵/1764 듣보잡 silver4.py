import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s1, s2 = set(), set()
for _ in range(n):
    s1.add(input().strip())
for _ in range(m):
    s2.add(input().strip())
result = s1.intersection(s2)
print(len(result))
for r in sorted(list(result)):
    print(r)