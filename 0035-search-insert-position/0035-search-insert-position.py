
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        hashset = set(nums)
        lens = len(nums)
        for i in range(0,len(nums)):
            
            if nums[i] == target:
                return i
            elif target not in hashset:
                if i + 1 < lens:
                    if target < nums[i+1] and target > nums[i]:   
                        return i+1
                elif target == nums[i] + 1 or target > nums[i] + 1:
                    return lens

            
        return 0