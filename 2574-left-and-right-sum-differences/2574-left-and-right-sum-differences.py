class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right = []
        left = []
        
        lSum = 0
        rSum = 0

        answer = []

        for i in range(len(nums)):
            right.append(rSum)
            rSum += nums[i]
            left.append(lSum)
            lSum += nums[len(nums)-1-i]

        for k in range(len(right)):
            answer.append(abs(right[k] - left[len(left)-1-k]))
            subs = 0


        return answer      