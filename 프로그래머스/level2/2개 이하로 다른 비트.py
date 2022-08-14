def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2:
            target = 2
            while number & target:
                target <<= 1
            answer.append(number ^ (target + (target >> 1)))
        else:
            answer.append(number + 1)
    return answer