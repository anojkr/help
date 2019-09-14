
class Solution:
	# @param A : list of integers
	# @return an integer
	def maxArr(self, A):
	    n = len(A)
	    max1 = -9999999999999999
	    max2 = -9999999999999999
	    min1 = 9999999999999999
	    min2 = 999999999999999
	    result = -999999999999999
	    
	    for i in range(n):
	        max1 = max(A[i] + i, max1)
	        min1 = min(A[i] + i, min1)
	        
	        max2 = max(A[i] - i, max2)
	        min2 = min(A[i] - i, min2)
	   
	    result = max(max1 - min1, result)
	    result = max(max2 - min2, result)
	    
	    return result

