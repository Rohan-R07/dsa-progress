from collections import Counter

class Solution:
    def findDuplicates(self, arr):
        # code here
        
        freq1 = Counter(arr)
        newList = []
        for key,value in freq1.items():
            if value > 1:
                newList.append(key)
                
        return newList