import sys
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        A.sort()
        if n == 0 or B == 0:
            return 0

        i = 0
        j = B-1
        res = sys.maxsize
        while j < n and i < n:
            diff = A[j] - A[i]
            res = min(diff, res)
            i+=1
            j+=1
            
        return res
            
