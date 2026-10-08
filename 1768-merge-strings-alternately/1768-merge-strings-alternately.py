class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1),len(word2)
        i,j = 0,0
        resultString = ""
        while i < n and j < m:

            resultString += word1[i]
            resultString += word2[j]
            i += 1
            j += 1

        if i < n:
            while i < n:
                resultString += word1[i]
                i += 1


        if j < m :
            while j < m:
                resultString += word2[j]
                j += 1

        return resultString
        
            
