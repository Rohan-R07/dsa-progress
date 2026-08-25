class Solution:
    def insertAtIndex(self, arr, index, val):
        # code here
        arr.append(0)
        for i in range(len(arr)-1,index,-1):
            arr[i] = arr[i-1]
            
        arr[index] = val
            