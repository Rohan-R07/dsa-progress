# class Solution:
#     def hasTripletSum(self, arr, target):
        # Code Here
        
        # arr.sort()
        


        # for i in range(len(arr)-2):
            
        #     left = i+1
        #     right = len(arr)-1
            
        #     while left <right:
        #         total = arr[i] + arr[left] + arr[right]
        #         if total < right:
        #             left += 1
                
        #         elif total > right:
        #             right -= 1
                
        #         else:
        #             return True 
            
        # return False
        
        
class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return True

        return False