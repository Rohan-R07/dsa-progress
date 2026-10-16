class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # it is here to remove the duplicate of i
                continue
            j = i+1
            k = len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1

                elif nums[i] + nums[j] + nums[k] >0:
                    k -= 1

                else:
                        result.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]: # THIS CODE IS USED TO REMOVE THE DUPLICATES of j 
                            j += 1
                
        return result

            
                