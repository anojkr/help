class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        
        n1 = len(A)
        n2 = len(B)

        for i in range(0, n1):
            if A[i:i+n2] == B:
                return i
        return -1