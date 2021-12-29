dic={0:1}

def t(n):
    if n in dic:
        return dic[n]
    
    else:
        result=0
        for i in range(1,n+1):
            result+=t(n-i)*t(i-1)
        dic[n]=result
        return dic[n]

print("%3s" % "n","     ","t(n)")
for n in range(0,101):
    print("%3d" % n,"     ",t(n))