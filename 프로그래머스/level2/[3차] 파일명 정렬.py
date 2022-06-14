import re

def solution(files):
    answer = []
    lst = []
    
    for i, file in enumerate(files):
        number = re.findall('[0-9]{1,5}', file)[0]
        idx = file.find(number)
        lst.append([file[:idx].lower(), int(file[idx:idx+len(number)].lower()), i])
    
    lst.sort()
    
    for l in lst:
        answer.append(files[l[2]])
        
    return answer