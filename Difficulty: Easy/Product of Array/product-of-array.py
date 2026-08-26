class Solution:
    def product(self, arr):
        # code here
        prod =  1
        for i in arr:
            
            prod *=  i
            
        if prod >1000000007:
            return prod % 1000000007
        return prod