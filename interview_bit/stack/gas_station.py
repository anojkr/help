Other method

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        if sum(B)>sum(A): return -1
        n=len(A)
        if n ==1 and B[0] == 0:
            return 0
        sur = 0
        dif = 0
        start = 0
        for i in range(0, n):
            sur = sur + A[i]-B[i]
            if sur < 0:
                sur = 0
                dif+=sur
                start = i+1
        if sur + dif >= 0:
            return start
        return -1



class Solution:
    # @param A : tuple of integers gas
    # @param B : tuple of integers distance
    # @return an integer
    def canCompleteCircuit(self, A, B):
        if sum(B)>sum(A): return -1
        n=len(A)
        
        ans=total=cost=0
        for i in range(n):
            total+=A[i]
            cost+=B[i]
            if cost>total:
                ans=(i+1)
                total=cost=0
        return ans 
