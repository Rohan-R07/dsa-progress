# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         seen = []
#         duplicate = []
#         for i in range(len(nums)):
#             if nums[i] not in seen:
#                 seen.append(nums[i])
   
        
#         for i in range(len(seen)):
#             nums.remove(seen[i])

#         return len(nums)
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for i in range(len(nums)):
            if nums[i] not in new_list:
                new_list.append(nums[i])
        
        for i in range(len(new_list)):
            nums[i] = new_list[i]
        return len(new_list)