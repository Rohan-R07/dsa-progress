class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right  = len(numbers) - 1
        result = []
        while left <right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]

            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] > target:
                right -= 1
        return result