class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        newList = []
        for i in range(len(matrix)):
            sums = sum(matrix[i])
                
            newList.append(sums)
            
        return newList