class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        
        left = nums1[:m]
        right = nums2[:n]
        i,j = 0,0
        ln,rn = len(left),len(right)
        result = []

        while i < ln and j < rn:
            if left[i] <= right[j]:
                result.append(left[i])
                i+= 1

            else:
                result.append(right[j])
                j += 1

        if i < ln:
            while i < ln:
                result.append(left[i])
                i += 1

        if j < rn :
            while j < rn:
                result.append(right[j])
                j += 1
        print(result)
        for i in range(len(result)):
            nums1[i] = result[i]