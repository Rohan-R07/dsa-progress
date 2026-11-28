class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        

        prefix = 0
        seen = {0:1}
        count = 0
        for i in nums:
            prefix += i

            required = prefix - goal

            if required in seen:
                count += seen[required] 
            
            seen[prefix] = seen.get(prefix, 0) + 1


        return count

        
