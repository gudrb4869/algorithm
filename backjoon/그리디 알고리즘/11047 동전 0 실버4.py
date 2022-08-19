n, k = map(int, input().split())
answer = 0
for a in sorted([int(input()) for _ in range(n)], reverse=True):
    div, k = divmod(k, a)
    answer += div
print(answer)