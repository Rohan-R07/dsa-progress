class Solution:
    def romanToInt(self, s: str) -> int:
        
        hasset = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000       
        }
        sums = 0

        for i in range(len(s) - 1):
  
            if hasset[s[i]]< hasset[s[i+1]]:
                sums -= hasset[s[i]]
            else:
                sums += hasset[s[i]]

        sums += hasset[s[-1]]
        return sums


        return sums