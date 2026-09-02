class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxNumber = max(candies)
        sums = 0
        newList = []
        for i in range(len(candies)):
            sums = candies[i] + extraCandies
            if sums >= maxNumber:
                newList.append(True)
            elif sums < maxNumber:
                newList.append(False)

        return newList