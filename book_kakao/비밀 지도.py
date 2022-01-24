n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
'''for i in range(n):
    temp = str(bin(arr1[i]|arr2[i]))[2:]
    temp = temp.replace("1", "#")
    temp = temp.replace("0", " ")
    result.append(temp)
'''
for i in range(n):
    result.append(
        bin(arr1[i]|arr2[i])[2:].zfill(n).replace('0',' ').replace('1','#')
    )    
print(result)