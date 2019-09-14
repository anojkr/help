import math
class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        n = A
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = math.factorial(2*n)/(math.factorial(2*n-n)*math.factorial(n))
        r = int(res/(n+1))
        return r
