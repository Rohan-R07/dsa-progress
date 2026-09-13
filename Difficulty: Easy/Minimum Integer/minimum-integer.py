class Solution:
    def minimumInteger(self, arr):
        # code here
        sums = sum(arr)
        smallest = 0
        n = len(arr)
        answer = []
        
        for i in arr:
            if sums <= n*i:
                answer.append(i)
            
        return min(answer)
            
        
            
        
        