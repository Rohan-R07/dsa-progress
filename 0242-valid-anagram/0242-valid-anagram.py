class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        frequency = {}

        for i in range(len(s)):
            if s[i] in frequency:
                frequency[s[i]] += 1
            else:
                frequency[s[i]] = 1
            
        frequency2 = {}
        for k in range(len(s)):
            if t[k] in frequency2:
                frequency2[t[k]] += 1
            else:
                frequency2[t[k]] = 1
        
        return frequency == frequency2
            