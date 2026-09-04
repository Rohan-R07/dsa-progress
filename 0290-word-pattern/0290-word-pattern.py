class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        sList = s.split()
        if len(sList) != len(pattern) : return False
        hashDict1 = dict()
        hashDict2 = dict()
        for i in range(len(pattern)):
            
            if (pattern[i] in hashDict1 and hashDict1[pattern[i]] != sList[i] ) or (sList[i] in hashDict2 and hashDict2[sList[i]] != pattern[i]):
                return False

            hashDict1[pattern[i]] = sList[i]
            hashDict2[sList[i]] = pattern[i]


        return True
