class Solution:
    def finalString(self, s: str) -> str:

        result = []
        n = len(s)
        for i in range(n):

            if s[i] == "i":
                result = result[::-1]

            else:
                result.append(s[i])


        return "".join(result)