class Solution:
    def reverse(self, x: int) -> int:

        absolute = abs(x)
        rev = 0
        while absolute > 0:
            lastDigt = absolute % 10
            rev = (rev*10) + lastDigt
            absolute = absolute//10
   
        if x > 0:
            if rev > 2147483647:
                return 0
            
            return rev 
        else:
            if rev > 2147483647:
                return 0
            return -rev