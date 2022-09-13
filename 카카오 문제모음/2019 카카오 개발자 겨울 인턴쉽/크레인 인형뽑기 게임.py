def solution(board, moves):
    stack, n = [], len(board)
    answer = 0
    l = [[b[i] for b in reversed(board) if b[i]] for i in range(n)]
    for i in moves:
        if l[i - 1]:
            cur = l[i - 1].pop()
            if stack and stack[-1] == cur:
                stack.pop()
                answer += 2
            else:
                stack.append(cur)
    return answer