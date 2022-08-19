import sys
input = sys.stdin.readline
time = sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[1], x[0]))
answer, cur = 1, time[0][1]
for start, end in time[1:]:
    if cur <= start:
        cur = end
        answer += 1
print(answer)