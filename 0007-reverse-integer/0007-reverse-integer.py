class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        temp = abs(x)  # work with positive version        
        while temp > 0:
            lastDigit = temp%10
            rev = rev * 10 + lastDigit
            if rev <= -2**31:
                return 0
            if rev >= 2**31-1:
                return 0
            temp = temp//10

        if x < 0:
            return -rev
        else:
            return rev
                


        
        

        