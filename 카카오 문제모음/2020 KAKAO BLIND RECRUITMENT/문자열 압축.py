def solution(s):
    n = len(s)
    answer = n
    for i in range(1, n//2 + 1):
        lst = [s[j:j+i] for j in range(0, n, i)]
        prev = ''
        result, cnt = '', 1
        for l in lst + ['']:
            if prev == l:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt)
                result += prev
                prev = l
                cnt = 1
        answer = min(answer, len(result))
    return answer