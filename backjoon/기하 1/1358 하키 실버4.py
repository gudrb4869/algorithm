W, H, X, Y, P = map(int, input().split())
answer = 0

def inlink(x, y):
    if X <= x <= X + W and Y <= y <= Y + H:
        return True
    if ((X - x) ** 2 + (Y + H // 2 - y) ** 2) ** 0.5 <= H // 2:
        return True
    if ((X + W - x) ** 2 + (Y + H // 2 - y) ** 2) ** 0.5 <= H // 2:
        return True
    return False

for _ in range(P):
    x, y = map(int, input().split())
    if inlink(x, y):
        answer += 1
print(answer)