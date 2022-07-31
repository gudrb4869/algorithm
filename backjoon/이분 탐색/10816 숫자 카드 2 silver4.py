from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
input()
a = sorted(list(map(int, input().split())))
input()
for i in list(map(int, input().split())):
    print(bisect_right(a, i) - bisect_left(a, i), end=' ')