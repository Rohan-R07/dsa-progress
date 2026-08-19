class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        duplicate = []
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate.append(nums[i])
            else:
                seen.add(nums[i])
        
        for k in duplicate:
            nums.remove(k)
        return len(nums)

        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen.append(nums[i])
            

        # print(seen)
        # return 0