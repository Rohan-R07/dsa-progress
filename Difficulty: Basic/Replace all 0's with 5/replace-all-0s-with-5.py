class Solution:
    def convertFive(self, n):
        digit = list(str(n))
        stringbud = ""
        for i in range(len(digit)):
            if digit[i] == "0":
                digit[i] = '5'
                stringbud += digit[i]
            else:
                stringbud += digit[i]
                
        return int(stringbud)
        
        
        # rev = 0
        # while n>0:
        #     lastDig = n%10
        #     if lastDig == 0:
        #         lastDig = 5
        #     rev = (rev*10) + lastDig
            
        # return rev
