class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        
        d = {}
        n = len(A)
        flag = 0
        curr_sum = 0
        for i in range(0, n):
            curr_sum += A[i]
            d[curr_sum] = i
            
            if curr_sum == B:
                return A[0: i+1]
                
            elif curr_sum - B in d:
                diff = curr_sum -B
                x = d[diff] +1
                return A[x : i+1]
                
        return [-1]
