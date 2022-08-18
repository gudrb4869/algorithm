n = int(input())
a = list(map(int, input().split()))
upper, lower = [0] * n, [0] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            upper[i] = max(upper[i], upper[j])
    upper[i] += 1

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[j] < a[i]:
            lower[i] = max(lower[i], lower[j])
    lower[i] += 1

answer = 0
for i in range(n):
    answer = max(answer, upper[i] + lower[i])
print(answer - 1)