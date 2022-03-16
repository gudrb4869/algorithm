from typing import List
from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dict = defaultdict(list)
    for str in strs:
        dict[''.join(sorted(str))].append(str)
    return list(dict.values())
    
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))