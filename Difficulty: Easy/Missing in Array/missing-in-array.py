class Solution:
    def missingNum(self, arr):
        hashs = set(arr)
        for i in range(1,max(hashs)+2):
            if i not in hashs:return i
            
