class Solution:
    def removeDuplicates(self, arr):
        # code here 
        
        result = set(arr)
        sortedResult = sorted(result)
        return sortedResult