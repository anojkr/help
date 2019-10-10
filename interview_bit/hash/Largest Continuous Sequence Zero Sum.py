class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sums = {0: 0}
        curSum = 0
        s = e = -1
        for i in range(len(A)):
            curSum += A[i]
            if curSum not in sums:
                sums[curSum] = i + 1
            elif i - sums[curSum] > e - s or s == -1:
                s = sums[curSum]
                e = i
        return A[s:e+1] 