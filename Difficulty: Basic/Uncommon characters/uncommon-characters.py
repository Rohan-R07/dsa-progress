from collections import Counter

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        
        freqS1 = Counter(s1)
        freqS2 = Counter(s2)
        strings = ""
        for i in freqS1:
            if i not in freqS2:
                strings += i
                
        for k in freqS2:
            if k not in freqS1:
                strings += k
                
        return "".join(sorted(strings))