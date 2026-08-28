
class Solution:
    def swapKth(self, arr, k):
        # Code Here
        last = arr[-k]
        first = arr[k-1]
        
        arr[k-1] = last
        arr[-k] = first
