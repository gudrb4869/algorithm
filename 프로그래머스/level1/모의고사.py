def solution(answers):
    result = []
    score = [0, 0, 0]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i, answer in enumerate(answers):
        if a[i % 5] == answer:
            score[0] += 1
        
        if b[i % 8] == answer:
            score[1] += 1
            
        if c[i % 10] == answer:
            score[2] += 1
    
    for i, s in enumerate(score):
        if s == max(score):
            result.append(i + 1)
    return result