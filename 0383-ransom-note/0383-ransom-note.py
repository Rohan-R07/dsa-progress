from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        frequencyRansom = Counter(ransomNote)

        # for i in range(len(ransomNote)):
        #     frequencyRansom[ransomNote[i]] = frequencyRansom.get(ransomNote[i],0)+1

        frequencyRansom1 = Counter(magazine)

        # for i in range(len(magazine)):
        #     frequencyRansom1[magazine[i]] = frequencyRansom1.get(magazine[i],0)+1
        
        for i in frequencyRansom:
            if i not in frequencyRansom1:
                return False
            if frequencyRansom[i] > frequencyRansom1[i]:
                return False

        return True
                
        
