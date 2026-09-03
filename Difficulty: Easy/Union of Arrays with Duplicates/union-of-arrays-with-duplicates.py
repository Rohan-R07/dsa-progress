from collections import Counter

class Solution:    
    def findUnion(self, a, b):
        # code here
        
        freq1 = set(a)
        freq2 = set(b)
        
        return list(freq1 | freq2)