from collections import Counter
n = int(input())
s = Counter(list(map(int, input().split())))
print(s[int(input())])