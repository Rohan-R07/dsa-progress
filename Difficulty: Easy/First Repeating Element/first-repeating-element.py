from collections import Counter

class Solution:
    def firstRepeated(self, arr):
        # code here 
        
        freq = Counter(arr)
        # duplicate
        # for key,value in freq.items():
        #     if value > 1:
        
        # print(freq)
                
        for i in range(len(arr)):
            if arr[i] in freq and freq[arr[i]] > 1:
                return i+1
                
        return -1