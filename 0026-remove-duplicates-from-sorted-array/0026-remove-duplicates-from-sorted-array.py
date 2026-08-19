class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        duplicate = []
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate.append(nums[i])
            else:
                seen.append(nums[i])
        
        for i in range(len(duplicate)):
            nums.remove(duplicate[i])
  
        return len(nums)
        
