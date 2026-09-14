from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        newList = []
        extraNum = 0
        for key, value in freq1.items():

            if key in freq2  :
                
                minium = min(freq2[key],value)

                for j in range(minium):
                    newList.append(key)

        return newList
            