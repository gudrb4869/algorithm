def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1], reverse=True)
    while routes:
        end = routes.pop()[1]
        while routes and routes[-1][0] <= end:
            routes.pop()
        answer += 1
    return answer