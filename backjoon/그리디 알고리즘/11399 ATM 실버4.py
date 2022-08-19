n = int(input())
answer = 0
for p in sorted(list(map(int, input().split()))):
    answer += p * n
    n -= 1
print(answer)