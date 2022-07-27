from collections import deque

def solution(begin, target, words):
    def compare(word1, word2):
        count = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                count += 1
        return count == 1
    
    q = deque([(begin, 0)])
    visited = []
    while q:
        cur, cnt = q.popleft()
        if cur == target:
            return cnt
        
        for word in words:
            if compare(cur, word) and word not in visited:
                visited.append(word)
                q.append([word, cnt + 1])
    
    return 0