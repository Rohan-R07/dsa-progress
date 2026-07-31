class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen = []
        duplicates = []

        for num in nums:
            if num in seen:
                if num not in duplicates:
                    duplicates.append(num)
            else:
                seen.append(num)

                
        temp =0
        for i in nums:
            if i not in duplicates:
                temp = i
            
        return temp
