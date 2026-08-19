class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        duplicate = []
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate.append(nums[i])
            else:
                seen.add(nums[i])
        
        for k in range(len(duplicate)):
            nums.remove(duplicate[k])
        return len(nums)
        
