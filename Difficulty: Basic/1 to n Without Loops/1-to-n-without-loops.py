class Solution:
    def printTillN(self, n):
    	#code here 
    	
    	def f(i,n):
    	    if i > n:
    	        return
    	    
    	    print(i,end=" ")
    	    f(i+1,n)
        f(1,n)