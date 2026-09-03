from collections import Counter
class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        
        freq = Counter(arr)
        
        keys = 0
        for key,value in freq.items():
            
            if value % 2 != 0:
                keys = key
            
        return keys
                