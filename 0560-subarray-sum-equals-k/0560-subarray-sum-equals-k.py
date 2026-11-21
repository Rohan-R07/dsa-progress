class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        seen = {0:1}
        count = 0

        for num in nums:

            prefix += num

            required = prefix-k

            if required in seen:
                count += seen[required]

            seen[prefix] = seen.get(prefix, 0) + 1

        return count
