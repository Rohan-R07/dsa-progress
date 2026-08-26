class Solution:
    def reverseArray(self, arr):
        # code here
        newList = arr.copy()
        for i in range(0,len(newList)):
            arr[i] = newList[len(arr)-i-1]
        
        