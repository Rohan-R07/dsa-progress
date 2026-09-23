from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        is_odd = False
        freq = Counter(s)
        for values in freq.values():
            if values %2 == 0:
                length += values

            else:
                length += values - 1
                is_odd = True

        if is_odd:
            length+= 1
        return length


