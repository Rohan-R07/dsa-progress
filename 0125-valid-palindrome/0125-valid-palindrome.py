class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = s.strip().lower()
        newString = ""
        for i in string:
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

