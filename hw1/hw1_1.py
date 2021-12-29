def Binary_Search(key):
    lo=0
    hi=len(arr)-1
    mid=(lo+hi)//2
    while lo<=hi:
        if key==arr[mid]:
            return mid+1
        elif key<arr[mid]:
            hi=mid-1
        elif key>arr[mid]:
            lo=mid+1
        mid=(lo+hi)//2
    return 'None'

arr = list(map(int,input().split()))
key = int(input())
print(Binary_Search(key))