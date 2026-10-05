class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for start in range(len(haystack) - len(needle) + 1): # eliminate the 
            found = True
            for j in range(len(needle)):
                
                if haystack[start+j] != needle[j]:
                    found = False
                    break

            if found:
                return start


        return -1