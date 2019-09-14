class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        pA = 0
        pB = 0
        pC = 0
        minmax = float("inf")
        while pA < len(A) and pB < len(B) and pC < len(C):
            minmax = min(minmax, max(abs(A[pA] - B[pB]), abs(B[pB] - C[pC]), abs(C[pC] - A[pA])))
            if A[pA] == min(A[pA], B[pB], C[pC]):
                pA += 1
            elif B[pB] == min(A[pA], B[pB], C[pC]):
                pB += 1
            else:
                pC += 1
        
        return minmax

