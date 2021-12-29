def merge(arr,l,m,r):
    result,i,j=[],l,m+1

    while i<=m and j<=r:
        if arr[i]<=arr[j]:
            result.append(arr[i])
            i+=1
        else:
            result.append(arr[j])
            j+=1
    if i>m:
        while j<=r:
            result.append(arr[j])
            j+=1
    else:
        while i<=m:
            result.append(arr[i])
            i+=1
    arr[l:r+1]=result

def mergesort(arr,l,r):
    if l<r:
        m=(l+r)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)

arr = list(map(int,input().split()))
mergesort(arr,0,len(arr)-1)
print(arr)