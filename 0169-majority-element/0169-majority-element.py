class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums) // 2
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
     

        for key,value in hashmap.items():
            if value > n:
                return key
