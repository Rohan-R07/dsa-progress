class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newList = []
        sums = 0
        for i in range(len(nums)):
            sums = sums+ nums[i]
            newList.append(sums)

        return newList