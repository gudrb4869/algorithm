# def solution(n):
#     ans = 0
#     while n != 1:
#         n, mod = divmod(n, 2)
#         ans += mod
#     return ans + 1

def solution(n):
    return bin(n).count('1')