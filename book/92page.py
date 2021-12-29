from typing import List

def numMatchingSubseq(self, S: str, words: List[str]) -> int:
    matched_count = 0

    for word in words:
        pos = 0
        for i in range(len(word)):
            # Find matching position for each character.
            found_pos = S[pos:].find(word[i])
            if found_pos < 0:
                matched_count -= 1
                break
            else: # If found, take step position forward.
                pos += found_pos + 1
        matched_count += 1
    
    return matched_count