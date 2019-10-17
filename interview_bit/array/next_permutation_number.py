class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, a):
        
        i = len(a) - 2
        while not (i < 0 or a[i] < a[i+1]):
            i -= 1
        if i < 0:
            sorting = sorted(a)
            return sorting
        j = len(a) - 1
        while not (a[j] > a[i]):
            j -= 1
        a[i], a[j] = a[j], a[i]        
        a[i+1:] = reversed(a[i+1:])  
        return a

# class Solution:
#     # @param A : list of integers
#     # @return the same list of integer after modification
#     def nextPermutation(self, A):
        
#         N = len(A)
#         i = N-1
#         if N == 1:
#             return A
#         while i >= 1:
#             if A[i-1] < A[i]:
#                 break
#             i -= 1
#         d1 = i-1
#         if d1 >=0:
#             res = d1+1
#             for k in range(d1+1, N):
#                 if A[d1] < A[k] and A[res] > A[k]:
#                         res = k
#             A[d1], A[res] = A[res], A[d1]
#             y = A[d1+1:N]
#             y.sort()
#             x = A[0:d1+1]
#             x.extend(y)
#             return x
#         else:
#             A.sort()
#             return A