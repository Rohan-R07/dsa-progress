from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        newList = []
        freq = Counter(nums)

        for key,value in freq.items():
            if value > (n/3):
                newList.append(key)

        return newList