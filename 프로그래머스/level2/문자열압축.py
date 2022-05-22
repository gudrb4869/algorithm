def solution(s):
    answer = 1000
    for i in range(1, len(s) + 1):
        results = []
        j = 0
        while j < len(s):
            cur = s[j : j + i]
            if results and results[-1][0] == cur:
                results[-1][1] += 1
            else:
                results.append([cur, 1])
            j += i
        length = 0
        for result in results:
            length += len(result[0])
            if result[1] > 1:
                length += len(str(result[1]))
        answer = min(answer, length)
    return answer