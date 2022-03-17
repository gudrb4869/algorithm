a, b, c = map(int, input().split())
d = int(input())
time = (a * 60 + b) * 60 + c + d
tmp, c = divmod(time, 60)
a, b = divmod(tmp, 60)
a %= 24
print(a, b, c)