class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[],[]]
        num1 = set(nums1)
        num2 = set(nums2)
        for n1 in num1:
            if n1 not in num2 and n1 not in answer[0]:
                answer[0].append(n1)

            
        for n2 in num2:
            if n2 not in num1 and n2 not in answer[1]:
                answer[1].append(n2)

            
        return answer

        