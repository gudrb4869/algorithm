import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        # print('left =', left, 'right =', right, 'counts =', counts)
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            # print()
            # print('left =', left, 'right =', right, 'counts =', counts)
            max_char_n = counts.most_common(1)[0][1]
            # print('max_char_n =', max_char_n)
            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
                # print('counts = ', counts, 'left =', left)
        return right - left

solution = Solution()
print(solution.characterReplacement('AABABBA', 1))