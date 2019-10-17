class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        
        result = [-1]*len(A)
        stack = []
        
        for i in range(0, len(A)):
            if len(stack) == 0 or A[stack[-1]] >= A[i]:
                stack.append(i)
            elif A[stack[-1]] < A[i]:
                while len(stack) >= 1 and A[stack[-1]] < A[i]:
                        result[stack.pop()] = A[i]
                stack.append(i)
        # print(stack)
        return result

