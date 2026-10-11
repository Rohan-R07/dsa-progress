class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        sortedVal = sorted(nums)

        left = 0
        right = len(nums) -1
        count = 0
        while left < right:
            if sortedVal[left] + sortedVal[right] < k:
                left += 1

            elif sortedVal[left] + sortedVal[right] > k:
                right -= 1

            else:
                left += 1
                right -= 1
                
                count += 1
        return count