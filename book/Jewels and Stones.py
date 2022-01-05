import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''
        freqs = {}
        count = 0

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count
        '''
        '''
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count
        '''
        '''
        freqs = collections.Counter(stones)
        count = 0
        for char in jewels:
            count += freqs[char]
        return count
        '''
        return sum(s in jewels for s in stones)
solution = Solution()
print(solution.numJewelsInStones(input("J = "), input("S = ")))