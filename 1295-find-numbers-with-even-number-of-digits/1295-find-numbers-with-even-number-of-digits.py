class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = ""
        even = 0
        for i in range(len(nums)):
            for k in range(len(str(nums[i]))):

                count = str(k)
            
            if (int(count)+1)%2 == 0:
                even+=1
        return even
            