2class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        
        n = A
        if n == 1:
            return 1
        t = [0 for i in range(n+1)]
        
        t[0] = 0
        t[1] = 1
        t[2] = 2
        for i in range(3, n+1):
            t[i] = t[i-1] + t[i-2] 
        return t[n]
        
