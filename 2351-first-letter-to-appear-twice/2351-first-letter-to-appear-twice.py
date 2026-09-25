class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        seen = []
        duplicate = ""

        for i in range(len(s)):

            if s[i] in seen :
                return s[i]
            else:
                seen.append(s[i])

 