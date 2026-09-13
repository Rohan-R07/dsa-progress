class Solution:
    def reverseWords(self, s: str) -> str:
        
        newString = s.strip().split()
        
        newList = ""
        for i in range(len(newString)-1,-1,-1):


            if i != 0:
                newList+=newString[i]+" "
            else:
                newList += newString[i]
        return newList