from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = Counter(arr)
        seen = []
        duplicate = []
        for key,value in freq.items():
            if value in seen:
                duplicate.append(value)
            else:
                seen.append(value)

        if len(duplicate) == 0:
            return True 
        else:
            return False
