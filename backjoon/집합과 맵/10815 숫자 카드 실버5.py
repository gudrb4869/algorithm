import sys
input = sys.stdin.readline
n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in list(map(int, input().split())):
    print('1' if i in s else '0', end=' ')