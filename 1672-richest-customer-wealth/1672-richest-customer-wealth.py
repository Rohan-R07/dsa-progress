class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        newList = []
        sums = 0
        for i in range(len(accounts)):
            for k in range(len(accounts[i])):
                sums += accounts[i][k]
            newList.append(sums)
            sums = 0

        return max(newList)
            