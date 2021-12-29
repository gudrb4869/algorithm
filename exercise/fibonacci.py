def memoize(f):
    memo={}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

fib=memoize(fib)
print("%3s" % "n", "   ","fibonacci")
for n in range(0,101):
    print("%3d" % n,"   ",fib(n))