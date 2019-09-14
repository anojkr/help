class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        
        d = {}
        
        res = set()
        
        for a in range(len(A)):
            if -A[a] not in d:
                d[-A[a]]=[a]
            else:
                d[-A[a]].append(a)
        
                
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                if A[i]+A[j] in d:
                    for a in d[A[i]+A[j]]:
                        if a != i and a != j:
                            cur = sorted([A[a],A[i],A[j]])
                            res.add(tuple(cur))
        
        return list(res)
	    
	    

