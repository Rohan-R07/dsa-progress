class Solution:
    def minMoves(self, nums: list[int]) -> int:

        #minium approach

        # minium = min(nums)

        # counter = 0
        # for i in range(len(nums)):
        #     counter += nums[i] - minium

        # return counter

        #maxium number approach

        maxium = min(nums)

        counter = 0
        for i in range(len(nums)):
            if nums[i] != maxium: 
                counter += maxium - nums[i]

        return abs(counter)

        