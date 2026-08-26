class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        new = s.strip().split()
        return len(new[-1])