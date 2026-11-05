class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        
        n = len(nums) 
        fast = 0
        slow = 0
        while fast < n:
            if nums[fast] % 2 == 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]

                slow += 1

            fast += 1

        return nums