from collections import Counter

class Solution:
    def frequencyCount(self, arr):
        #  code here
        
        answer = []
        freq = Counter(arr)
        
        
        
        for i in range(1,len(arr)+1):
            if i not in freq:
                freq[i] = 0
        
        
        sortedVer = sorted(freq.items(),key=lambda x:x[0],reverse = False)
        
        for i,k in sortedVer:
            answer.append(k)
        
        return answer