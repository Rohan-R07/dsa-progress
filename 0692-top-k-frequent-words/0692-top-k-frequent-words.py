from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = Counter(words)
        newList = list(freq.items())

        sortedVal = sorted(newList, key=lambda x: (-x[1], x[0])) # GOD KNOWS HOW
        topFreq = []
        for i in range(k):
            topFreq.append(sortedVal[i][0])
        return topFreq