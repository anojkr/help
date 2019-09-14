class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 1:
            return n
        size = n
        j = 1
        prev = A[0]
        for i in range(j,n):
            if A[i] != prev:
                prev = A[i]
                A[j] = A[i]
                j += 1
                
        return j
            

