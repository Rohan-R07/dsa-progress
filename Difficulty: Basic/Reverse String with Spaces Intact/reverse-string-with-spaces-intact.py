class Solution:
    def reverses(self, s):
        # code here
        
        left = 0
        right = len(s) -1
        
        newString = list(s)
        
        while left < right:
            if newString[left] == " ":
                left += 1
                continue
            
            if newString[right] == " ":
                right -= 1
                continue
            
            newString[left],newString[right] = newString[right],newString[left]
            
            # s.replace(s[left],s[right])
            left += 1
            right -= 1
            
        strs = ""
        for i in newString:
            strs += i
        return strs
            
        
            
            