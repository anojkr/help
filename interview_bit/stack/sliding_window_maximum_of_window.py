from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        # print(A)
        n = len(A)
        C = [int(x) for x in A]
        t = 0
        r = deque()
        res = []
        if n == 1 and B == 1:
            return C
        for x in range(0, n):
            r.append(C[x])
            t = t + 1
            if t == B:
                res.append(max(r))
                r.popleft()
                t = t -1
                continue
            
        return res
            
            
            
            
