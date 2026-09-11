class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        nonZeros = []
        # for i in nums:
        #     if i == 0:
        #         zeros.append(0)
        #         break
        #     nonZeros.append(i)

        # newArr = nonZeros + zeros
        # for k in range(len(newArr)):
        #     nums[i] = newArr[i]

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(nums[i])
            else:
                nonZeros.append(nums[i])
        newArr = nonZeros + zeros

        for i in range(len(newArr)):
            nums[i] = newArr[i]
            
        
