class Solution:
	def twoSum(self, arr, target):
		# code 
		
		seen = set()
		
		
		for i in range(len(arr)):
		    needed = target-arr[i]
		    if needed in seen:
		        return True
		    seen.add(arr[i])
        return False