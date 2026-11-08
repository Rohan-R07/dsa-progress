class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        newList = list(s)
        

        for i in range(0,len(newList), 2*k):
            left = i
            right = min(i + k, len(newList)) - 1

            while left < right:

                newList[left],newList[right] = newList[right],newList[left]

                left += 1
                right -= 1

        

        return "".join(newList)

