p = [0,1,1]
for _ in range(3, 101):
    p.append(p[-2] + p[-3])
for _ in range(int(input())):
    print(p[int(input())])