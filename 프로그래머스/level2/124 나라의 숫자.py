def solution(n):
    answer = ''
    dic = {0:'1', 1:'2', 2:'4'}
    while n > 0:
        n -= 1
        n, mod = divmod(n, 3)
        answer += dic[mod]
        
    return answer[::-1]