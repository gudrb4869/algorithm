from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    s1 = Counter([str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    s2 = Counter([str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()])
    
    a = sum((s1 & s2).values())
    b = sum((s1 | s2).values())
    return 65536 if a == b == 0 else int(a / b * 65536)