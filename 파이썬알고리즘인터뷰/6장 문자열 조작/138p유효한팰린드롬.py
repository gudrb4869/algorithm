import collections

def isPalindrome(s: str) -> bool:
    strs = collections.deque()

    for c in s:
        if c.isalnum():
            strs.append(c.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))