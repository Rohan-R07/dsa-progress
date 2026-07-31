class Solution:
    def isPalindrome(self, x: int) -> bool:

        xs = str(x)
        rev = xs[::-1]
        if xs == rev:
            return True
        else:
            return False

