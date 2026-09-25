class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        

        # duplicate = []
        # # for i in range(len(nums)):
        # #     if nums[i] in seen:
        # #         duplicate.append(nums[i])
        # #     else:
        # #         seen.append(nums[i])
        

        # nums.sort()
        # removeDup = set(sorted(nums))
        # removedList = list(removeDup)

        hashing = set(nums)

        newList = list(hashing)
        newList.sort()
        if len(newList) < 3:
            return max(newList)
        
        return newList[-3]
        