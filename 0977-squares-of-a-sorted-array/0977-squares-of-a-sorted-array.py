class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        newList = []
        for i in range(len(nums)):
            sqare = nums[i] * nums[i]
            newList.append(sqare)

        newList.sort()
        return newList