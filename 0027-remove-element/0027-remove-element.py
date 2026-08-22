class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        duplicate = list(nums)
        for i in duplicate:
            if i == val:
                nums.remove(i)
            

        return len(nums)