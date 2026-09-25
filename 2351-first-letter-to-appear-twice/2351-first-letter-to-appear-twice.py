from collections import Counter

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        string = ""
        freq = Counter(s)

        seen = []
        duplicate = ""

        for i in range(len(s)):

            if s[i] in seen :
                duplicate = s[i]
                break
            else:
                seen.append(s[i])

        for key,elements in freq.items():
            if key == duplicate:
                return key