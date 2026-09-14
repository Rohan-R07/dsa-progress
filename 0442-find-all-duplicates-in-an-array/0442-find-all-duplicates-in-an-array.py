from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        freq = Counter(nums)
        newList = []
        for key,value in freq.items():
            if value >1:
                newList.append(key)


        return newList