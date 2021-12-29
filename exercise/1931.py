t=[list(map(int,input().split()))for i in range(int(input()))]
t.sort(key=lambda x:x[0])
t.sort(key=lambda x:x[1])
m=c=0
for i in t:
 if i[0]>=m:c+=1;m=i[1]
print(c)