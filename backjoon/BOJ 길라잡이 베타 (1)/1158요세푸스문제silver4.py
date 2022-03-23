n, k = map(int, input().split())
queue, result = [], []
for i in range(1, n + 1):
    queue.append(i)
cur = 0
while queue:
    cur = (cur + k - 1) % len(queue)
    result.append(queue.pop(cur))
print('<' + str(result)[1:-1] + '>')