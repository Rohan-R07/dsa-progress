class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	newList = []
    	n = len(arr)
    	for i in range(n):
    	    if arr[i] !=0:
    	        newList.append(arr[i])
        
        for k in range(len(newList),len(arr)):
            newList.append(0)
        
        for i in range(len(newList)):
            arr[i] = newList[i]
        