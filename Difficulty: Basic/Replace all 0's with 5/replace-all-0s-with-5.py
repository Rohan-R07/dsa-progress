class Solution:
    def convertFive(self, n):
        # code her e
        digit = list(str(n))
        stringbud = ""
        for i in range(len(digit)):
            if digit[i] == "0":
                digit[i] = '5'
                stringbud += digit[i]
            else:
                stringbud += digit[i]
                
        return int(stringbud)
