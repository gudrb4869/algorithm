n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
if n <= 2:
    print(sum(s))
    exit(0)
d = [0] * (n + 1)
d[1], d[2] = s[0], s[0] + s[1]
for i in range(3, n + 1):
    d[i] = max(d[i - 3] + s[i - 2] + s[i - 1], d[i - 2] + s[i - 1])
print(d[-1])