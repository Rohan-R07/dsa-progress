class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        example = []
        for i in range(0,len(nums)):
            for j  in range(i,-1,-1):
                if i != j :
                    if nums[i] + nums[j] == target:
                        example = [i,j]
                        break
                        
        return example