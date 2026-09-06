from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        freq1 = Counter(s)
        freq2 = Counter(t)
        for key,value in freq2.items():
            if key not in freq1:
                return key
            elif value > freq1[key]:
                return key