class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        

        seen = []
        duplicate = []
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate.append(nums[i])
            else:
                seen.append(nums[i])
        
        
        seen.sort()
        print(seen)

        if len(seen) < 3:
            return max(seen)
        
        return seen[-3]
        