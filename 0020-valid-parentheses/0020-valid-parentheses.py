
class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()
        for charss in s:
            if len(s) == 1:
                return False
            else :
                if charss == "(":
                    stack.append(")")

                elif charss == "[":
                    stack.append("]")

                elif charss == "{":
                    stack.append("}")

                elif charss == "]":
                    
                    if not stack or stack[-1] != charss:
                        return False
                    stack.pop()
                    
                elif charss == ")":
                    
                    if not stack or stack[-1] != charss:
                        return False
                    stack.pop()

                elif charss == "}":
                    
                    if not stack or stack[-1] != charss:
                        return False
                    stack.pop()
            


        if not stack:
            return True
        else:
            return False
                

       