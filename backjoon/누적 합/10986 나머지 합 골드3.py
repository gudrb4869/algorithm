import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
mod = [0] * m
answer, sum = 0, 0
for a in arr:
    sum = (sum + a) % m
    mod[sum] += 1
for i in range(m):
    answer += mod[i] * (mod[i] - 1) // 2
answer += mod[0]
print(answer)