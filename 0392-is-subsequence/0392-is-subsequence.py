class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        spointer , tpointer = 0,0
        n,m = len(s),len(t)
        while spointer<n and tpointer < m:
            if s[spointer] == t[tpointer]:
                spointer += 1

            tpointer += 1

        return spointer == n
