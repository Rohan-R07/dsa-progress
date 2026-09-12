class Solution:
    def sortString(self, s: str) -> str:
        # code here
        
        newStr = sorted(s)
        
        string = ""
        
        for i in newStr:
            string += i
        return string