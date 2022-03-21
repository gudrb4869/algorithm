import sys
input = sys.stdin.readline

def binary_search(target):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if card[mid] == target:
            return True
        elif card[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
lsts = list(map(int, input().split()))
for lst in lsts:
    if binary_search(lst):
        print('1', end=' ')
    else:
        print('0', end=' ')