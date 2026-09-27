class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <2: return False
        factorial = [1]
        for i in range(2,int(sqrt(num))+1):
            if num % i == 0 : 
                factorial.append(i)

                if num//i != num: factorial.append(num//i)

        
        return sum(factorial) == num


        