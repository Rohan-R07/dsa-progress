class Solution:
    def leaders(self, arr):
        # code here
        newList = []
        greatest = float("-inf")
        for i in range(len(arr)-1,-1,-1):
            if arr[i] >= greatest:
                newList.append(arr[i])
                greatest = arr[i]
        
        return newList[::-1]
        
        
        # leaders = []
        # max_seen = float("-inf")

        # for i in range(len(arr) - 1, -1, -1):
        #     if arr[i] >= max_seen:
        #         leaders.append(arr[i])
        #         max_seen = arr[i]

        # leaders.reverse()
        # return leaders