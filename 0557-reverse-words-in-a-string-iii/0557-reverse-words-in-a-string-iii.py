class Solution:
    def reverseWords(self, s: str) -> str:
        
        newList = s.split()
        answer = ""
        for i in newList:
            reversedList = i[::-1]+" "
            answer += reversedList


        
        return answer.strip()