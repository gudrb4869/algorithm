def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            k, _ = stack.pop()
            answer[k] = i - k
        stack.append((i, price))
    for i, _ in stack:
        answer[i] = len(prices) - i - 1
    return answer