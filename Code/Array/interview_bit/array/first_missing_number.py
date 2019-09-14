

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A = list(filter(lambda x : x > 0, A))
        A = [len(A) + 2] + A
        for i, num in enumerate(A):
            num = abs(num)
            if num < len(A):
                A[num] = - abs(A[num])
        for i in range(1, len(A)):
            if A[i] > 0:
                return i
        return len(A)

