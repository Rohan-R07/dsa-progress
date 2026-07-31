class Solution:
    def isPalindrome(self, s: str) -> bool:

        sa = "Rohan"
        cleaned = []
        for c in s:
            if c.isalnum():
                print(c.isalnum())
                cleaned.append(c.lower())


        rev = []
        for i in range(len(cleaned)-1,-1,-1):
            rev.append(cleaned[i])

        if cleaned == rev:
            return True

        else:
            return False