class Solution:
    def isPalinArray(self, arr):
         # code here
        answer = False
        for i in arr:
            no = str(i)
            
            if no == no[::-1]:
                answer = True
            else:
                answer = False
                break
        return answer
        