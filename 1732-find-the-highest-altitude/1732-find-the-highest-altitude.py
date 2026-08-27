class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        newList = [0]
        sums = 0
        for i in range(len(gain)):
            sums += gain[i]
            newList.append(sums)
        return max(newList)