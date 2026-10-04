class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            
            if i != "*":
                stack.append(i)

            if i == "*":
                stack.pop()
        result = ""
        for i in stack:
            result += i

        return result