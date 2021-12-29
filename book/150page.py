s = ['2 A', '1 B', '4 C', '1 A']

# def func(x):
#     return x.split()[1], x.split()[0]

# s.sort(key=func)
s.sort(key=lambda x: (x.split()[1], x.split()[0]))
print(s)