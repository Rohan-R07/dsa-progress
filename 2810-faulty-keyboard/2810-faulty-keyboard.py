class Solution:
    def finalString(self, s: str) -> str:

        result = []
        n = len(s)
        for i in range(n):

            if s[i] == "i":
                result.reverse()

            else:
                result.append(s[i])


        return "".join(result)