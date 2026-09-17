class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer1 = []
        answer2 = []

        for n1 in range(len(nums1)):
            if nums1[n1] not in nums2 and nums1[n1] not in answer1:
                answer1.append(nums1[n1])

            
        for n2 in range(len(nums2)):
            if nums2[n2] not in nums1 and nums2[n2] not in answer2:
                answer2.append(nums2[n2])

            
        return [answer1,answer2]

        