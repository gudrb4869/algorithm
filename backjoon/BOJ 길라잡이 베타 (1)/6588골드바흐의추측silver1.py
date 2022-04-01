import sys

sieve =  [True] * 1000001
for i in range(3, 1001, 2):
    if sieve[i] == True:
        for j in range(i + i, 1000001, i):
            sieve[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    flag = 0
    a, b = 3, n - 3
    while a <= b:
        if sieve[a] and sieve[b]:
            print(n, '=', a, '+', b)
            flag = 1
            break
        else:
            a += 2
            b -= 2
    if flag == 0:
        print("Goldbach's conjecture is wrong.")