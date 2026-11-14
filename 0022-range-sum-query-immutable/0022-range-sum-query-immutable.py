class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]*len(nums)
        self.prefix[0] = nums[0]

        for su in range(1,len(nums)):
            self.prefix[su] = self.prefix[su-1] + nums[su]

    def sumRange(self, left: int, right: int) -> int:
        sums = 0
        if left == 0:
            return self.prefix[right] 
        return self.prefix[right] - self.prefix[left-1] 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)