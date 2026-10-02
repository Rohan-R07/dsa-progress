class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        
        left = nums1[:m]
        right = nums2[:n]
        i,j = 0,0
        ln,rn = len(left),len(right)
        nums1.clear()
        result = []

        while i < ln and j < rn:
            if left[i] <= right[j]:
                nums1.append(left[i])
                i+= 1

            else:
                nums1.append(right[j])
                j += 1

        if i < ln:
            while i < ln:
                nums1.append(left[i])
                i += 1

        if j < rn :
            while j < rn:
                nums1.append(right[j])
                j += 1
