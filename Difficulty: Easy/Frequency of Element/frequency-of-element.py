from collections import Counter

class Solution:
    def findFrequency(self, arr, x):
        # code here
        
        freq = Counter(arr)
        
        for key,value in freq.items():
            
            if key == x:
                return value
                
        return 0