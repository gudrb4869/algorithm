from itertools import combinations
while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    for result in list(combinations(s, 6)):
        print(*result)
    print()