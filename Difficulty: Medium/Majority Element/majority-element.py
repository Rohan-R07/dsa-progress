from collections import Counter

class Solution:
    def majorityElement(self, arr):
        #code here
        
        freq = Counter(arr)
        majority = 0
        n = len(arr)
        majorityKey = []
        for key,element in freq.items():
            if element > (n//2):
                majorityKey.append(key)
                
        if len(majorityKey) == 1:
            return majorityKey[0]
            
        return -1