

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        i = j = result = 0
        sz = len(A)
        storage = set()
    
        while i < sz and j < sz:
            if A[j] in storage:
                storage.remove(A[i])
                i += 1
            else:
                storage.add(A[j])
                j += 1
                result = max(result, j-i)
    
        return result

