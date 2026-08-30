class Solution:
    def findIndex (self, arr, key):
        #code here
        newList = []
        for i in range(len(arr)):
            if arr[i] == key:
                newList.append(i)
        
        if len(newList) == 1:
            return newList*2
        elif len(newList) >= 2:
            return [newList[0],newList[len(newList)-1]]
        else:
            return [-1,-1]