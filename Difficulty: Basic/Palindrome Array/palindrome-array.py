class Solution:
    def isPalindrome(self, arr):
        # code here
        revArr = arr[::-1]
    
        if arr == revArr:
            return True
        else:
            return False
            
