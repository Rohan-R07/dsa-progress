class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        newList = []
        for i in range(len(matrix)):
            sums = 0
            for k in range(len(matrix[i])):
                sums += matrix[i][k]
                
            newList.append(sums)
            
        return newList