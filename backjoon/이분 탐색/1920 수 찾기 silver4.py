import sys
input = sys.stdin.readline

def binary_search(i):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == i:
            return 1
        elif a[mid] > i:
            high = mid - 1
        else:
            low = mid + 1
    return 0

input()
a = sorted(list(map(int, input().split())))
input()
for i in list(map(int, input().split())):
    print(binary_search(i))