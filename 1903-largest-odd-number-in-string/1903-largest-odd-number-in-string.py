class Solution:
    def largestOddNumber(self, num: str) -> str:
        newOdd = ""
        for numbers in range(len(num)-1,-1,-1):
            if int(num[numbers]) % 2 != 0 :
                return num[:numbers+1]

        return ""
            
                

        