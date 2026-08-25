class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tempStr = s.copy()
        n = len(tempStr)
        for i in range(n):
            s[i] = tempStr[n-i-1]
