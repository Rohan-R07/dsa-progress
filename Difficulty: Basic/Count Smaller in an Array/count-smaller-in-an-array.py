class Solution:
    def countOfElements(self, x, arr):
        # code here
        
        output = 0
        
        for i in arr:
            if i <= x:
                output += 1
                
        return output