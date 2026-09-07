class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current = 0
        newList = []
        for i in nums:

            if i == 1:
                current += 1
            else:
                newList.append(current)
                current = 0

        newList.append(current)
        return max(newList)