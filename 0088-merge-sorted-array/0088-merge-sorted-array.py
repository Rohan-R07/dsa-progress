class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        
        left = nums1[:m]
        right = nums2[:n]
        nums1.clear() 

        nl ,rl = len(left),len(right)
        
        leftP,rightP = 0,0
        while leftP < nl and rightP < rl:
            if left[leftP] <= right[rightP]:
                nums1.append(left[leftP])
                leftP += 1

            else:
                nums1.append(right[rightP])
                rightP += 1


        if leftP < nl:
            while leftP <nl:
                nums1.append(left[leftP])
                leftP += 1

        if rightP < rl:
            while rightP < rl:
                nums1.append(right[rightP])
                rightP += 1


