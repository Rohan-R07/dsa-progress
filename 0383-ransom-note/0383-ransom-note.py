from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        frequencyRansom = Counter(ransomNote)
        frequencyRansom1 = Counter(magazine)
        
        for i in frequencyRansom:
            if i not in frequencyRansom1:
                return False
            if frequencyRansom[i] > frequencyRansom1[i]:
                return False

        return True
                
        
