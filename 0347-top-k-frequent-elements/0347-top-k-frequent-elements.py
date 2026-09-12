from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        newList = []
        minIndex = 0
        
        sorting = sorted(freq.items(),key=lambda x : x[1], reverse = True)
        
        for i in range(k):
            newList.append(sorting[i][0])
        
        return newList
