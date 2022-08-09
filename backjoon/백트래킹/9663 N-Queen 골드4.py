def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def nQueen(x):
    global answer
    if x == n:
        answer += 1
    else:
        for i in range(n):
            row[x] = i
            if promising(x):
                nQueen(x + 1)

n = int(input())
row = [0] * n
answer = 0
nQueen(0)
print(answer)