class Solution:
    def findElements(self,arr):
        # code here
        largest = arr[0]
        secLargest = 0
        
        # for i in range(len(arr)):
        #     if largest < arr[i]:
        #         secLargest = largest
        #         largest = arr[i]
            
        #     elif secLargest < arr[i]:
        #         secLargest = arr[i]
                
        # arr.remove(largest)
        # arr.remove(secLargest)
        
        # return arr
        arr.sort()
        newSort = sorted(arr)
        
        newSort.remove(arr[-1])
        newSort.remove(arr[-2])

        
        return newSort