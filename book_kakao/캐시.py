'''cacheSize = int(input())
cities = list(map(str, input().split()))
result = 0
cache = []

if cacheSize == 0:
    result = len(cities) * 5
else:
    for city in cities:
        if city.lower() not in cache:
            result += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city.lower())
        else:
            result += 1
            cache.append(cache.pop(cache.index(city.lower())))
print(result)'''

import collections
cacheSize = int(input())
cities = list(map(str, input().split()))
cache = collections.deque(maxlen=cacheSize)
elapsed: int = 0

for c in cities:
    c = c.lower()
    if c in cache:
        cache.remove(c)
        cache.append(c)
        elapsed += 1
    else:
        cache.append(c)
        elapsed += 5

print(elapsed)