import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

node = []

def post_order(left, right):
    if left <= right:
        mid = right + 1
        for cur in range(left + 1, right + 1):
            if node[left] < node[cur]:
                mid = cur
                break
        post_order(left + 1, mid - 1)
        post_order(mid, right)
        print(node[left])

while True:
    try:
        n = int(input())
        node.append(n)
    except:
        break

post_order(0, len(node) - 1)