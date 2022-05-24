import re
from collections import Counter

def solution(str1, str2):
    s1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if re.findall('[a-z]{2}', str1[i:i+2].lower())]
    s2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if re.findall('[a-z]{2}', str2[i:i+2].lower())]            
    
    intersection = sum((Counter(s1) & Counter(s2)).values())
    union = sum((Counter(s1) | Counter(s2)).values())
    
    if union == 0:
        return 65536
    
    return int((intersection / union) * 65536)