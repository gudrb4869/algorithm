for _ in range(int(input())):
    lst = list(map(str, input().split()))
    num = float(lst.pop(0))
    for l in lst:
        if l == "@":
            num *= 3
        elif l == "%":
            num += 5
        elif l == "#":
            num -= 7
    print(f"{num:.2f}")