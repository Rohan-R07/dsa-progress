class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tempStr = s.copy()
        for i in range(len(tempStr)):
            s[i] = tempStr[len(s)-i-1]
