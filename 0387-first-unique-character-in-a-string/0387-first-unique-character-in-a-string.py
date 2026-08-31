class Solution:
    def firstUniqChar(self, s: str) -> int:

        frequency = {}
        for i in range(len(s)):
            if s[i] in frequency:
                frequency[s[i]] += 1
            else:
                frequency[s[i]] = 1
        newVar = ""
        for key,value in frequency.items():
            if value == 1:
                newVar = key
                break
        for i in range(len(s)):
            if s[i] == newVar:
                return i
        return -1

        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         return i
        # return -1