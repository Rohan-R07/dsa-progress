class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        #PREFIX SUM APPROACH
        n = len(gain)
        prefix = [0] * (n+1)
        

        for i in range(0,n):
            prefix[i + 1] = prefix[i] + gain[i]

        return max(prefix)


        #OLD APPROACH 

        # newList = [0]
        # sums = 0
        # for i in range(len(gain)):
        #     sums += gain[i]
        #     newList.append(sums)
        # return max(newList)


