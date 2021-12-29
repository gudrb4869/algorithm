a=[]
x=int(input())
for i in range(x):
    num, start, end = map(int, input().split())
    a.append([num,[start,end]])
a.sort(key=lambda x:x[1][0])
a.sort(key=lambda x:x[1][1])
t=0
result=[]
for i in range(x):
    if t <= a[i][1][0]:
        t = a[i][1][1]
        result.append(a[i][0])
print(result)