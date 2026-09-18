from collections import Counter

class Solution:
    def findTwoElement(self, arr):
        # code here

        duplicate = 0
        missing = 0
        seen = set()
        newArr = set(arr)

        for i in range(len(arr)+1):
            
            if i not in newArr:
                missing = i
                
    
            
            
        for i in range(len(arr)):
            if  arr[i] in seen:
                duplicate = arr[i]
                break
            else:
                seen.add(arr[i])
                
        
        
        return [duplicate,missing]