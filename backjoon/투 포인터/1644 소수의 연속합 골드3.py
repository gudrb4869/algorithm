def prime_list(n):
    sieve = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i+i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

n = int(input())
a = prime_list(n)
left, cur, answer = 0, 0, 0
for right in range(len(a)):
    cur += a[right]
    while cur > n and left < right:
        cur -= a[left]
        left += 1
    if cur == n:
        answer += 1
print(answer)