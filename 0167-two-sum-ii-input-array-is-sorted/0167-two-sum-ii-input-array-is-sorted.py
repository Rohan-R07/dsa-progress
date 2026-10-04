class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right  = len(numbers) - 1
        result = []
        while left <right:
            if numbers[left] + numbers[right] == target:
                result.append(left+1)
                result.append(right+1)
                break

            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] > target:
                right -= 1
        return result