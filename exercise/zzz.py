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

'''priorities = [2,1,3,2]
location = 2

queue = priorities[:]
queue.sort(reverse=True)

lst = []

for i, p in enumerate(priorities):
    lst.append((p, i))

answer = 0
while True:
    if queue[0] == lst[0][0]:
        answer += 1
        if location == lst[0][1]:
            break
        queue.pop(0)
        lst.pop(0)
    else:
        lst.append(lst.pop(0))

print(answer)'''

'''priorities = [2,1,3,2]
location = 2
queue = [(i,p) for i,p in enumerate(priorities)]
answer = 0
while True:
    cur = queue.pop(0)
    if any(cur[1] < q[1] for q in queue):
        queue.append(cur)
    else:
        answer += 1
        if cur[0] == location:
            break
print(answer)'''

'''bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
answer = 0

waiting = [[w,0] for w in truck_weights]
queue = []
while waiting or queue:
    if waiting and (not queue or weight >= sum(q[0] for q in queue) + waiting[0][0]):
        queue.append(waiting.pop(0))

    answer += 1
    for q in queue:
        q[1] += 1
    print("queue =", queue, "answer =", answer)
    if queue[0][1] == bridge_length:
        queue.pop(0)

answer += 1
print(answer)'''

'''prices = [1,2,3,2,3]
answer = [0]*len(prices)

for i in range(len(prices) - 1):
    for j in range(i+1, len(prices)):
        answer[i] += 1
        if prices[i] > prices[j]:
            break

print(answer)'''

'''prices = [1,2,3,2,3]
size = len(prices)
answer = [0] * size
stack = []

for i in range(size):
    while stack and prices[stack[-1]] > prices[i]:
        answer[stack[-1]] = i - stack[-1]
        stack.pop()
    stack.append(i)

while stack:
    answer[stack[-1]] = size - stack[-1] - 1
    stack.pop()
print(answer)'''

'''import heapq
scoville = [1,2,10,9,3,12]
K = 7
answer = 0
heapq.heapify(scoville)

while any(K > s for s in scoville):
    if len(scoville) <= 1:
        print(-1)
        break
    new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
    heapq.heappush(scoville, new)
    answer += 1

print(answer)'''

'''import heapq
jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
size = len(jobs)
jobs.sort()
heap = []
total_time = 0
current_time = 0
while jobs or heap:
    if not heap:
        request_time, elapsed_time, waiting_time = jobs[0][0], jobs[0][1], 0
        current_time += request_time - current_time
        jobs.pop(0)
    else:
        elapsed_time, request_time = heapq.heappop(heap)
        waiting_time = current_time - request_time
    
    print('request_time =', request_time, 'elapsed_time =', elapsed_time, 'waiting_time =', waiting_time, 'current_time =', current_time)
    
    while jobs and jobs[0][0] <= current_time + elapsed_time:
        heapq.heappush(heap, (jobs[0][1], jobs[0][0]))
        jobs.pop(0)
    current_time += elapsed_time
    total_time += elapsed_time + waiting_time
    print('total_time =', total_time)

print(total_time // size)'''

'''operations = ["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]
heap = []
for operation in operations:
    if operation[0] == "I":
        heap.append(int(operation[2:]))
        heap.sort()
    elif operation[0] == "D":
        if not heap:
            continue
        
        if operation[2:] == "-1":
            heap.pop(0)
        elif operation[2:] == "1":
            heap.pop()

if not heap:
    print([0,0])
else:
    print([max(heap), min(heap)])'''

'''array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
result = []
for command in commands:
    lst = array[command[0] - 1 : command[1]]
    lst.sort()
    result.append(lst[command[2] - 1])
print(result)'''

'''array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
print(list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1],commands)))'''
'''import functools
numbers = [0,0,0,0]
numbers = list(map(str, numbers))
numbers.sort(key=functools.cmp_to_key(lambda x,y: int(x+y)-int(y+x)),reverse=True)
result = str(int(''.join(numbers)))
print(result)'''
'''numbers = [3,9,30,5,34]
numbers = list(map(str, numbers))
numbers.sort(key=lambda x: x*3,reverse=True)
result = str(int(''.join(numbers)))
print(result)'''
'''citations = [0, 1, 1, 3, 3, 5, 6, 7, 11, 13, 111, 1111, 10000]
citations.sort()
size = len(citations)
print(citations)
for i, citation in enumerate(citations):
    if citation >= size - i:
        print(size - i)
        break
print(0)'''
'''citations = [1,5,0,6,4]
citations.sort(reverse=True)
answer = max(map(min, enumerate(citations, start=1)))
print(answer)'''
'''answers = [1,2,3,4,2]
s1 = {0:1, 1:2, 2:3, 3:4, 4:5}
s2 = {0:2, 1:1, 2:2, 3:3, 4:2, 5:4, 6:2, 7:5}
s3 = {0:3, 1:3, 2:1, 3:1, 4:2, 5:2, 6:4, 7:4, 8:5, 9:5}
dic = {1:0, 2:0, 3:0}

result = []
for i in range(len(answers)):
    if answers[i] == s1[i%5]:
        dic[1] += 1
    if answers[i] == s2[i%8]:
        dic[2] += 1
    if answers[i] == s3[i%10]:
        dic[3] += 1

dic = list(dic.items())
dic.sort(key= lambda x: -x[1])
print(dic)
result.append(dic[0][0])
for i in range(1, len(dic)):
    if dic[i][1] < dic[0][1]:
        break
    result.append(dic[i][0])
print(result)'''
'''answers = [1,2,3,4,5]
p1 = [1,2,3,4,5]
p2 = [2,1,2,3,2,4,2,5]
p3 = [3,3,1,1,2,2,4,4,5,5]
score = [0,0,0]
result = []
for i, answer in enumerate(answers):
    if answer == p1[i%5]:
        score[0] += 1
    if answer == p2[i%8]:
        score[1] += 1
    if answer == p3[i%10]:
        score[2] += 1

for i, s in enumerate(score):
    if s == max(score):
        result.append(i+1)
print(result)'''
'''from itertools import permutations
from math import sqrt
def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

numbers = "17"
lst = []
for i in range(1, len(numbers) + 1):
    lst.extend(map(int, map(''.join, permutations(numbers, i))))
lst = sorted(list(set(lst)))
result = 0
for v in lst:
    if is_prime_number(v):
        result += 1
print(result)'''
'''import math
brown, yellow = 8, 1
def func(x):
    lst = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            lst.append((x//i, i))
    return lst
lst1 = func(brown+yellow)
# print(lst1)
lst2 = func(yellow)
# print(lst2)
for (m, n) in lst1:
    if (m-2, n-2) in lst2:
        print([m, n])
        break'''
'''n = 3
lost = [1,2]
reserve = [2,3]
result = 0
lost, reserve = list(set(lost).difference(set(reserve))), list(set(reserve).difference(set(lost)))
print(lost)
print(reserve)
for i in range(1, n+1):
    if i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            result += 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            result += 1
    else:
        result += 1

print(result) '''

'''name = "ABAAABAAAAAAAAABA"문제 이상함!!!!!!!!!!!!!!!!!!! 그리디 조이스틱
move = len(name) - 1
result = 0
left, right = 0, 0
while name[move] == 'A' and move > 0:
    move -= 1

for i, c in enumerate(name):
    result += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    right = i + 1
    
    while right < len(name) and name[right] == 'A':
        right += 1
    
    move = min(move, i + i + (len(name) - right))

result += move
print(result)'''
'''number = "19809"
k = 3
answer = []
for num in number:
    while k > 0 and answer and answer[-1] < num:
        answer.pop()
        k -= 1
    answer.append(num)

print(''.join(answer[:len(answer) - k]))'''
'''from collections import deque
people = [70,50,80]
limit = 100
deq = deque(sorted(people))
answer = 0
while deq:
    if len(deq) == 1:
        answer += 1
        break
    if deq[0] + deq[-1] <= limit:
        deq.pop()
        deq.popleft()
    else:
        deq.pop()
    answer += 1
print(answer)'''
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
'''costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]
n = 5
costs = sorted(costs, key=lambda x: x[2])
parent = [-1 for _ in range(n)]
answer = 0
def find(x):
    if parent[x] < 0: return x
    parent[x] = find(parent[x])
    return parent[x]
def merge(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] += parent[y]
        parent[y] = x

def isUnion(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    return False
    
for cost in costs:
    if isUnion(cost[0], cost[1]):
        continue
    merge(cost[0], cost[1])
    answer += cost[2]
print(parent)
print(answer)'''
# routes = [[-20,-15],[-14,-5],[-18,-13],[-5,-3]]
# routes = [[-10,-6],[-9,-8],[-9,-7],[-8,-6]]
'''routes = [[1,1],[0,0],[-1,1]]
routes = sorted(routes, key=lambda x: x[1])
print(routes)
count = 0
cur = -30001
for route in routes:
    if cur < route[0]:
        count += 1
        cur = route[1]
print(count)'''
# from collections import defaultdict
# N = 5
# number = 12
# dp = defaultdict(list)
# print(dp)
# ops = ['*', '//', '+', '-']
# for i in range(1, 9):
#     lst = []
#     lst.append(str(N)*i)
#     for j in range(1, i):
#         for x in dp[j]:
#             for y in dp[i - j]:
#                 for op in ops:
#                     if op == '//' and y == '0':
#                         continue
#                     lst.append(str(eval(x+op+y)))
#     dp[i] = list(set(lst))
#     if str(number) in dp[i]:
#         print(i)
#         break
# print(dp)
# print(-1)
'''triangle = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
# print(len(triangle))
for i in range(1, len(triangle)):
    triangle[i][0] += triangle[i - 1][0]
    triangle[i][i] += triangle[i - 1][i - 1]
    for j in range(1, i):
        triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
print(max(triangle[-1]))'''
# from collections import deque
# m, n, puddles = 4, 5, [[1,5],[2,3],[4,2]]
# dp = [[0]*(n+1) for _ in range(m+1)]
# visit = [[True]*(n+1) for _ in range(m+1)]
# dp[1][1] = 1
# queue = deque()
# queue.append([1,1])
# while queue:
#     [x, y] = queue.popleft()
#     right = [x, y+1]
#     down = [x+1, y]
    
#     if x <= m and y+1 <= n and visit[x][y+1] and [x, y+1] not in puddles:
#         queue.append([x, y+1])
#         visit[x][y+1] = False
#         dp[x][y+1] = (dp[x][y] + dp[x-1][y+1]) %1000000007

#     if x+1 <= m and y <=n and visit[x+1][y] and [x+1, y] not in puddles:
#         queue.append([x+1, y])
#         visit[x+1][y] = False
#         dp[x+1][y] = (dp[x+1][y-1] + dp[x][y]) % 1000000007
#     print(queue)
# print(dp[m][n])
# money = [1,2,3,1]
'''money = [1,2,3,1,5]
dp_1 = [0 for _ in range(len(money))] # 첫번째 집을 턴 경우
dp_2 = [0 for _ in range(len(money))] # 첫번째 집을 안 턴 경우
dp_1[0], dp_1[1] = money[0], money[0]
dp_2[1] = money[1]
for i in range(2, len(money) - 1):
    dp_1[i] = max(dp_1[i - 2] + money[i], dp_1[i - 1])
for i in range(2, len(money)):
    dp_2[i] = max(dp_2[i - 2] + money[i], dp_2[i - 1])
print(dp_1)
print(dp_2)
answer = max(dp_1[-2], dp_2[-1])
print(answer)'''
# numbers = [1,1,1,1,1]
# target = 3
# answer = 0
# result = 0
# def bfs(numbers, result):
#     global answer
#     if not numbers:
#         if result == target:
#             answer += 1
#         return
#     bfs(numbers[1:], result - numbers[0])
#     bfs(numbers[1:], result + numbers[0])
# bfs(numbers, result)
# print(answer)
'''n = 3
computers = [[1,1,0],[1,1,1],[0,1,1]]
answer = 0
parent = [-1 for _ in range(n)]
def find(x):
    if parent[x] < 0: return x
    parent[x] = find(parent[x])
    return parent[x]
def merge(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] += parent[y]
        parent[y] = x
for i in range(n):
    for j in range(i + 1,n):
        if computers[i][j] == 0 or find(i) == find(j):
            continue
        merge(i, j)

for p in sorted(parent):
    if p >= 0:
        break
    answer += 1
print(answer)'''
# from collections import deque
# begin = "hit"
# target = "cog"
# answer = 0
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# def solution(begin, target, words):
#     answer = 0
    
#     if target not in words:
#         return 0
    
#     def compare_words(w1, w2):
#         diff = 0
#         for i in range(len(w1)):
#             if w1[i] != w2[i]:
#                 diff += 1
#         return diff == 1

#     queue = deque()
#     queue.append((begin,0))
#     visited = []
#     while queue:
#         current, count = queue.popleft()
#         if current == target:
#             return count
            
#         for word in words:
#             if compare_words(current, word) and word not in visited:
#                 queue.append((word, count + 1))
#                 visited.append(word)
#     return 0
    
# print(solution(begin, target, words))
'''tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
from collections import defaultdict
tickets = [["SFO", "ICN"], ["ICN", "ATL"], ["ICN", "SFO"]]
def solution(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('ICN')
    return route[::-1]
print(solution(tickets))'''
# n = 6
# times = [7, 10]
# answer = 1e18
# left, right = 0, n * max(times)
# while left <= right:
#     mid = (left + right) // 2
#     done_num = 0
#     done_num = sum(mid//time for time in times)
#     if done_num >= n:
#         answer = min(answer, mid)
#         right = mid - 1
#     else:
#         left = mid + 1
# print(answer)
'''distance = 25
rocks = [2,14,11,21,17]
n = 2
rocks.sort()
left, right = 1, distance
answer = 0

while left <= right:
    mid = (left + right) // 2
    last_offset = 0
    rock_cnt = 0

    for i in range(len(rocks) - 1):
        if rocks[i] - last_offset >= mid:
            last_offset = rocks[i]
            rock_cnt += 1
    
    if rocks[-1] - last_offset >= mid and distance - rocks[-1] >= mid:
        rock_cnt += 1
    
    if rock_cnt >= len(rocks) - n:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)'''
# from collections import defaultdict, deque
# graph = defaultdict(list)
# n = 6
# vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# for a, b in sorted(vertex):
#     graph[a].append(b)
#     graph[b].append(a)
# dist = [0 for _ in range(n + 1)]
# visited = [True for _ in range(n + 1)]
# visited[1] = False
# queue = deque()
# queue.append(1)
# while queue:
#     current = queue.popleft()
#     for i in graph[current]:
#         if visited[i]:
#             visited[i] = False
#             dist[i] = dist[current] + 1
#             queue.append(i)
# print(dist)
# print(visited)
# print(graph)
# print(dist.count(max(dist)))
'''from collections import defaultdict
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
cnt = defaultdict(int)
answer = n

for win, lose in results:
    arr[win][lose] = 1
    arr[lose][win] = -1
    cnt[win] += 1
    cnt[lose] += 1

cnt = [x[0] for x in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))]

for c in cnt:
    win, lose = [], []
    for i, v in enumerate(arr[c]):
        if v == -1:
            lose.append(i)
        elif v == 1:
            win.append(i)
    
    for i in win:
        for j in lose:
            arr[i][j] = -1
            arr[j][i] = 1

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if arr[i][j] == 0:
            cnt += 1
        if cnt > 1:
            answer -= 1
            break
print(answer)'''
# from collections import defaultdict
# n = 5
# results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# answer = 0
# win, lose = defaultdict(set), defaultdict(set)
# for w, l in results:
#     lose[l].add(w)
#     win[w].add(l)

# print(win)
# print(lose)

# for i in range(1, n + 1):
#     for winner in lose[i]:
#         win[winner].update(win[i])
#     for loser in win[i]:
#         lose[loser].update(lose[i])

# print(win)
# print(lose)
# for i in range(1, n + 1):
#     if len(win[i]) + len(lose[i]) == n - 1:
#         answer += 1
# print(answer)
'''n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
for i in range(n):
    result.append(
        bin(arr1[i]|arr2[i])[2:].zfill(n).replace('0', ' ').replace('1', '#')
    )
print(result)'''
# dartResult = input()
# nums = [0]
# answer = 0
# for s in dartResult:
#     if s == 'S':
#         nums[-1] **= 1
#         nums.append(0)
#     elif s == 'D':
#         nums[-1] **= 2
#         nums.append(0)
#     elif s == 'T':
#         nums[-1] **= 3
#         nums.append(0)
#     elif s == '*':
#         nums[-2] *= 2
#         if len(nums) > 2:
#             nums[-3] *= 2
#     elif s == '#':
#         nums[-2] *= -1
#     else:
#         nums[-1] = nums[-1] * 10 + int(s)
#         continue

# print(sum(nums))
'''from collections import deque
cacheSize = int(input())
cache = deque(maxlen=cacheSize)
elapsed = 0
cities = list(map(str, input().split()))
for c in cities:
    c = c.lower()
    if c in cache:
        cache.remove(c)
        cache.append(c)
        elapsed += 1
    else:
        cache.append(c)
        elapsed += 5
print(elapsed)'''
n, t, m = map(int, input().split())
timetable = list(map(str, input().split()))
timetable = [
    int(time[:2]) * 60 + int(time[3:])
    for time in timetable
]
timetable.sort()

current = 540
for _ in range(n):
    for _ in range(m):
        if timetable and timetable[0] <= current:
            candidate = timetable.pop(0) - 1
        else:
            candidate = current
        
    current += t
h, m = divmod(candidate, 60)
print(str(h).zfill(2) + ':' + str(m).zfill(2))
