class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        #TRADITIONAL METHORD

        # newList = []
        # sums = 0
        # for num in nums:
        #     sums += num
        #     newList.append(sums)

        # return newList


        #PREFIX SUM METHORD 

        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]

        for i in range(1,n):

            prefix[i] = prefix[i-1] + nums[i]

        return prefix