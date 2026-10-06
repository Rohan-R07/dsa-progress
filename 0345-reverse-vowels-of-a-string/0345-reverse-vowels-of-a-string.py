class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowel = ["a","e","i","o","u"]
        left = 0
        right = len(s)-1
        newString = list(s)
        while left<right:

            if newString[left].lower() not in vowel:
                left += 1
                continue

            if newString[right].lower() not in vowel:
                right -= 1
                continue

            newString[left],newString[right] = newString[right],newString[left]
            right -= 1
            left +=1
        
        string = ""
        for j in newString:
            string += j

        return string
