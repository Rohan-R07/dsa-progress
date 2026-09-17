class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[],[]]

        for n1 in nums1:
            if n1 not in nums2 and n1 not in answer[0]:
                answer[0].append(n1)

            
        for n2 in nums2:
            if n2 not in nums1 and n2 not in answer[1]:
                answer[1].append(n2)

            
        return answer

        