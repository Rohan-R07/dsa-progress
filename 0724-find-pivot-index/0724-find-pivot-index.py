class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculation prefix
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        for i in range(len(nums)):
            leftSum = prefix[i-1] if i > 0 else 0

            rightSum = prefix[n-1] - prefix[i]

            if leftSum == rightSum:
                return i
 

        return -1

            