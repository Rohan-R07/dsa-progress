# class Solution:
#     def getMinMax(self, arr):
#         # code here
        
#         maxium = arr[0]
#         minumu = arr[0]
#         for i in range(len(arr)):
            
#             if arr[i] > maxium:
#                 maxium = arr[i]
                
#             if arr[i] < minumu:
#                 miniumu = arr[i]
            
            
#         return [minumu,maxium]


class Solution:
    def getMinMax(self, arr):

        maxium = arr[0]
        minumu = arr[0]

        for i in range(len(arr)):

            if arr[i] > maxium:
                maxium = arr[i]

            if arr[i] < minumu:
                minumu = arr[i]

        return [minumu, maxium]