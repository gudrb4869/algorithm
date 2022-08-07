import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dic = defaultdict(int)
for a in arr:
    dic[a] += 1
m = int(input())
for i in list(map(int, input().split())):
    print(dic[i], end=' ')