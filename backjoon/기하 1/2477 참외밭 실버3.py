import sys
input = sys.stdin.readline
k = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
w, h = [0, 0], [0, 0]
for i, (d, l) in enumerate(lst):
    if d < 3 and w[1] < l:
        w = [i, l]
    elif d > 2 and h[1] < l:
        h = [i, l]
print((w[1] * h[1] - lst[(w[0] + 3) % 6][1] * lst[(h[0] + 3) % 6][1]) * k)