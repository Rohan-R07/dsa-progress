class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        string = list(s)
        for i in range(len(string)):
            last = string[-1]

            for k in range(len(string)-1,0,-1):
                string[k] = string[k-1]

            string[0] = last

            if string == list(goal):
                return True
            
        return False
