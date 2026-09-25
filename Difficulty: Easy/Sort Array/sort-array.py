class Solution:
    def sortArr(self, arr): 
        # code here
        # #Bubble sorting bruhh
        # n = len(arr)
        # for i in range(n-2,-1,-1):
        #     for j in range(0,i+1):
        #         if arr[j] > arr[j+1]:
        #             arr[j],arr[j+1] = arr[j+1],arr[j]
                    
                    
        # INSERTION SORTING
        
        # n = len(arr)
        
        # for i in range(1,n):
        #     key = arr[i]
        #     j = i-1
            
        #     while j >= 0 and arr[j] > key:
        #         arr[j+1] = arr[j]
        #         j -= 1
            
        #     arr[j+1] = key
        
        
        arr.sort()