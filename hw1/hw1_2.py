def partition(arr,l,r):
    pivotitem=arr[l]
    j=l

    for i in range(l+1, r+1):
        if arr[i] < pivotitem:
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[l],arr[j]=arr[j],arr[l]
    return j

def quicksort(arr,l,r):
    if l<r: # arr:list l:left r:right p:pivotpoint
        p = partition(arr,l,r)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,r)


arr = list(map(int, input().split()))
quicksort(arr,0,len(arr)-1)
print(arr)