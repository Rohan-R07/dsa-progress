from collections import Counter

class Solution:
    def getMaxOccuringChar(self, s):
        # code here
        string = list(s)
        freq1 = Counter(s)
        maxium = max(freq1.values())
        result = []
        for key,element in freq1.items():
            if element == maxium:
                result.append(key)
                
        result.sort()
        
        if len(result) != 0:
            return result[0]
        else:
            string.sort()
            return string[0]