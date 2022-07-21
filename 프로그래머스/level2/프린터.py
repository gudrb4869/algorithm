from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    priorities.sort()

    while queue:
        key, value = queue.popleft()
        if value == priorities[-1]:
            answer += 1
            priorities.pop()
            if key == location:
                break
        else:
            queue.append((key, value))
            
    return answer