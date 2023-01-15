from itertools import product

def solution(users, emoticons):
    answer = []
    for rates in list(product([10, 20, 30, 40], repeat=len(emoticons))):
        cnt, cost = 0, 0
        for rate, price in users:
            total = 0
            for e, r in zip(emoticons, rates):
                if r >= rate:
                    total += e * (1 - r / 100)
            if total >= price:
                cnt += 1
            else:
                cost += total
        answer.append((cnt, cost))
    return sorted(answer)[-1]