class Solution:
    def largest(self, arr):
        # code here
        large = arr[0]
        
        for i in range(len(arr)):
            if arr[i] > large:
                large = arr[i]
            
        return large
