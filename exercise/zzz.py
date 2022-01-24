'''from math import ceil
from collections import deque

rem_day = deque([5,10,1,1,20,1])
answer = []
cur = rem_day.popleft()
count = 1
while rem_day:
    if cur >= rem_day[0]:
        count += 1
        rem_day.popleft()
    else:
        answer.append(count)
        count = 1
        cur = rem_day.popleft()
answer.append(count)
print(answer)'''
