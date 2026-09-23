from math import sqrt
class Solution:
    def isPerfect(self, n):
        # code here 
        sums = 1
        
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                sums += i
            

                if i != n // i:
                    sums += n // i
        
        return sums == n