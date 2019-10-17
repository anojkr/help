class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
	    
	    h = {}
	    
	    for i in range(0, len(A)):
	        if A[i] in h:
	            h[A[i]] +=1
	            continue
	        h[A[i]] = 1
	    res = []
	    for i in range(0, len(B)):
	        if B[i] in h:
	            if h[B[i]] >=1:
	                res.append(B[i])
	                h[B[i]]-=1
	    return res
	        
