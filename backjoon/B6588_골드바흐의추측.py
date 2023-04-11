import sys
input = sys.stdin.readline

a = [True for _ in range(1000001)]

for i in range(2, 1001):
    for j in range(i + i, 1000001, i):
        a[j] = False

def check(n):
    for i in range(3, n // 2 + 1, 2):
        if a[i] and a[n - i]:
            print(f'{n} = {i} + {n - i}')
            return
    print("Goldbach's conjecture is wrong.")

while True:
    n = int(input())
    if n == 0:
        break
    check(n)