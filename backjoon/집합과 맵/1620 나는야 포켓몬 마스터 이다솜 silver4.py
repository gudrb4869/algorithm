import sys
input = sys.stdin.readline
dic = {}
n, m = map(int, input().split())
for i in range(n):
    name = input().strip()
    dic[i + 1] = name
    dic[name] = i + 1
for _ in range(m):
    s = input().strip()
    if s.isdigit():
        print(dic[int(s)])
    else:
        print(dic[s])