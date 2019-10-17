class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        
        left = [0]*n
        right = [0]*n
        
        max_x = -sys.maxsize
        tax_x = -sys.maxsize

        for k in range(0, n):
            left[k] = max_x
            max_x = max(max_x, A[k])
            
        for k in range(n-1, -1, -1):
            right[k] = tax_x
            tax_x = max(tax_x, A[k])

        for k in range(0, n):
            if left[k] <= A[k] and A[k] >= right[k]:
                return A[k]
            
            
            