class Solution:
	def removeDuplicates(self, s):
	    # code here
	    
	    removed=""
	    duplicate = []
	    
	    for i in s:
	       if i in removed:
	           duplicate += i
	       else:
	           removed += i
	           
	    return removed
	           