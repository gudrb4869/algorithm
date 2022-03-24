import sys, math
input = sys.stdin.readline
n = int(input())
l1, l2 = [], []
result = 0
for _ in range(n):
    l1.append(int(input()))
l1.sort()
for i in range(1, n):
    l2.append(l1[i] - l1[i - 1])
min_dist = math.gcd(*l2)
for i in range(len(l2)):
    result += (l2[i] - min_dist) // min_dist
print(result)