class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dictS,dictT = {},{}

        for i in range(len(s)):
            dS,dT = s[i],t[i] 

            if (dS in dictS and dictS[dS] != dT) or (dT in dictT and dictT[dT] != dS):
                return False
            dictS[dS] = dT
            dictT[dT] = dS

        return True