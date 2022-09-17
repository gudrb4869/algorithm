from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
        else:
            cache.remove(city)
            answer += 1
        cache.append(city)
    return answer