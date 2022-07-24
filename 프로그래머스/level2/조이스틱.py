def solution(name):
    answer = 0
    n = len(name)
    move = n - 1
    for i in range(n):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
        move = min(move, min(i * 2 + n - j, (n - j) * 2 + i))
    
    return answer + move