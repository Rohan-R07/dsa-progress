class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        
        sStack = []
        tStack = []

        for i in range(len(s)):

            if s[i] == "#" and sStack:
                sStack.pop()
            
            if s[i] != "#":
                sStack.append(s[i])


        for j in range(len(t)):

            if t[j] == "#" and tStack:
                tStack.pop()

            if t[j] != "#":
                tStack.append(t[j])

        print(sStack,tStack)
        return "".join(sStack) == "".join(tStack)


        
        

        
            