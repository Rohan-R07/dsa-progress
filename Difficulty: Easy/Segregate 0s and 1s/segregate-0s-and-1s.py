class Solution:
    def segregate0and1(self, arr):
        # code here
        zeroes = []
        ones = []
        
        for i in range(len(arr)):
            if arr[i] == 0:
                zeroes.append(arr[i])
            else:
                ones.append(arr[i])
                
        newList = zeroes + ones
        for i in range(len(newList)):
            arr[i] = newList[i]
        