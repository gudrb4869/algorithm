import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
results = []
def dfs(k: int, result: int, plus, minus, mul, div):
    if k == n:
        results.append((result))
        return
    if plus:
        dfs(k + 1, result + a[k], plus - 1, minus, mul, div)
    if minus:
        dfs(k + 1, result - a[k], plus, minus - 1, mul, div)
    if mul:
        dfs(k + 1, result * a[k], plus, minus, mul - 1, div)
    if div:
        dfs(k + 1, int(result / a[k]), plus, minus, mul, div - 1)
        
        
dfs(1, a[0], op[0], op[1], op[2], op[3])
print(max(results))
print(min(results))