class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        
        B = list(A)
        n = len(A)
        t = [1]*n
        
        for i in range(1, n):
            for j in range(0, i):
                if A[i] > A[j] and t[i] < t[j]+1:
                    t[i] = t[j]  + 1
        return max(t)