from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        groups = {}

        for alpha in strs:
            key = "".join(sorted(alpha))

            if key not in groups:
                groups[key] = []

            groups[key].append(alpha)
        return list(groups.values())
