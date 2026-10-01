class Solution:
    def search(self, arr, x):
        # code here
        
        for index,element in enumerate(arr):
            if element == x:
                return index
                
        return -1