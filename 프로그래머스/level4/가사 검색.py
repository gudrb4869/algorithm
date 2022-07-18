# 1 이진탐색 이용한 풀이
'''
from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    dic, reverse_dic = defaultdict(list), defaultdict(list)
    for word in words:
        dic[len(word)].append(word)
        reverse_dic[len(word)].append(word[::-1])
    
    for v in dic.values():
        v.sort()
    for v in reverse_dic.values():
        v.sort()
        
    for query in queries:
        if query[0] == '?':
            lst = reverse_dic[len(query)]
            start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')
        else:
            lst = dic[len(query)]
            start, end = query.replace('?', 'a'), query.replace('?', 'z')
        answer.append(bisect_right(lst, end) - bisect_left(lst, start))
    return answer
'''
# 2 Trie 이용한 풀이
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        node.count += 1
        for w in word:
            node = node.children[w]
            node.count += 1
        
    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return 0
            node = node.children[w]
        return node.count

def solution(words, queries):
    answer = []
    trie, reverse_trie = defaultdict(Trie), defaultdict(Trie)
    
    for word in words:
        trie[len(word)].insert(word)
        reverse_trie[len(word)].insert(word[::-1])
    
    for query in queries:
        new_query = query.replace('?', '')
        if query[0] == '?':
            answer.append(reverse_trie[len(query)].search(new_query[::-1]))
        else:
            answer.append(trie[len(query)].search(new_query))
            
    return answer