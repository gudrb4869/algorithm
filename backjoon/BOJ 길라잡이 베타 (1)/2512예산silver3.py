import sys
input = sys.stdin.readline

n = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
m = int(input())

while True:
    n = len(l)
    mid = m // len(l)
    cur = l[-1]
    while cur <= mid:
        m -= l.pop()
        if not l:
            print(cur)
            exit(0)
        cur = l[-1]
    if n == len(l):
        print(mid)
        exit(0)