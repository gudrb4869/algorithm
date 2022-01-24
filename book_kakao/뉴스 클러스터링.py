'''str1 = input()
str2 = input()

set1 = set()
set2 = set()

str1 = str1.upper()
str2 = str2.upper()

for i in range(len(str1) - 1):
    if str1[i:i+2].isalpha():
        set1.add(str1[i:i+2])

for i in range(len(str2) - 1):
    if str2[i:i+2].isalpha():
        set2.add(str2[i:i+2])

try:
    print(int(len(set1.intersection(set2))/len(set1.union(set2)) * 65536))
except ZeroDivisionError:
    print("65536")'''

import collections, re

str1 = input()
str2 = input()

str1s = [
    str1[i:i+2].lower()
    for i in range(len(str1) - 1)
    if re.findall('[a-z]{2}', str1[i:i+2].lower())
]
str2s = [
    str2[i:i+2].lower()
    for i in range(len(str2) - 1)
    if re.findall('[a-z]{2}', str2[i:i+2].lower())
]

intersection = sum((collections.Counter(str1s) & collections.Counter(str2s)).values())

union = sum((collections.Counter(str1s) | collections.Counter(str2s)).values())

jaccard_sim = 1 if union == 0 else intersection / union
print(int(jaccard_sim * 65536))