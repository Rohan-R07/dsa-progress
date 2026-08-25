class Solution:
    def getAlternates(self, arr):
        # Code Here
        newList = []
        for i in range(len(arr)):
            
            if i % 2 == 0:
                newList.append(arr[i])
            
        
        return newList