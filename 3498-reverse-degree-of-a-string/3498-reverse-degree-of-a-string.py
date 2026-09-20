class Solution:
    def reverseDegree(self, s: str) -> int:

        # alphabets = "zyxwvutsrqponmlkjihgfedcba"
        # alphabetsDic = {}

        # for j in range(len(alphabets)):
            
        #     alphabetsDic[alphabets[j]] = alphabetsDic.get(alphabets[j],j+1)

        
        # sums = 0
        # for index,element in enumerate(s):
        #     sums += (index+1) * (alphabetsDic[element])

        # return sums
        sums = 0
        for i in range(len(s)):
            sums += (123-ord(s[i])) * (i+1)
        return sums