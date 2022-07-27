import sys
input = sys.stdin.readline
s = set()
n, m = map(int, input().split())
answer = 0
for _ in range(n):
    s.add(input())
for _ in range(m):
    t = set()
    t.add(input())
    if len(s.intersection(t)):
        answer += 1
print(answer)