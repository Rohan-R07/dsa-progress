from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)   
        freqList = list(freq.items())
        sortedStr = sorted(freqList,key = lambda x:x[1],reverse = True)

        newDict = dict(sortedStr)
        strings = ""
        for key,element in newDict.items():

            for i in range(element):
                strings += key

        return strings