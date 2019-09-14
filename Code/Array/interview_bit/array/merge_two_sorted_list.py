

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        i1, j1 = 0, len(A)-1
        i2, j2 = 0, len(B)-1
        A.extend([None]*len(B))
        k = len(A) - 1
        while j2 >= 0 and j1 >= 0:
            if A[j1] > B[j2]:
                A[k] = A[j1]
                j1 -= 1
            else:
                A[k] = B[j2]
                j2 -=1
            k -= 1
        while j2 > -1:
            A[k] = B[j2]
            k -= 1
            j2 -= 1
                
        return A

