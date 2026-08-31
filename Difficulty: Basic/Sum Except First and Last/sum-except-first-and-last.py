class Solution:
    def sumExceptFirstLast(self,arr):
        # code here
        sums = 0
        for i in range(1,len(arr)-1):
            sums += arr[i]
            
        return sums