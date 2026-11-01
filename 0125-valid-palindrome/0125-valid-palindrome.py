class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        newString = ""
        for i in s.strip().lower():
            if i.isalnum():
                newString += i
        left = 0
        right = len(newString) - 1
        while left < right:
            if newString[left] != newString[right]:
                return False

            left+= 1
            right -= 1

        return True 

