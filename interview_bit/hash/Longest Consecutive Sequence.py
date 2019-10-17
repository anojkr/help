class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        
        h = {}
        for x in A:
            if x in h:
                h[x] +=1
            else:
                h[x] = 1
                
        res = 0
        for i in range(0, len(A)):
            
            if A[i]-1 not in h:
                j = A[i]
                count = 0
                while (j in h):
                    j+=1
                    count+=1
                res = max(res, count)
        return res
        
        