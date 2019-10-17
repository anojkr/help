
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
       # for i in range(len(A)):
        while A != A[::-1]:
            A = A[:-1]
            count+=1
        return count

