class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        # nums.sort()
        # print(nums)

        # return (nums[-2] - 1) * (nums[-1] - 1)

        first = nums[0]
        second = 0
        for i in range(1,len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second:
                second = nums[i]
        print(first, second)
        return (first-1) *(second-1)