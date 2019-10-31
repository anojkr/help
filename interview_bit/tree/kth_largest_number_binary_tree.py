
def find_nlargest(root, n, c):

	if root == None:
		return None

	nlargest = find_nlargest(root.right, n, c)

	if nlargest == None:
		c = c + 1

		if n == c:
			nlargest = root

	if nlargest == None:
		nlargest = find_nlargest(root.left, n, c)

	return nlargest


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    C = 0
    
    def kth_smallest(self, A, B):
        if A == None:
            return None
            
        ksmallest = self.kth_smallest(A.left, B)
        
        if ksmallest == None:
            self.C = self.C + 1
            if self.C == B:
                ksmallest = A
                
        if ksmallest == None:
            ksmallest = self.kth_smallest(A.right, B)
            
        return ksmallest
    
    def kthsmallest(self, A, B):
        
        return self.kth_smallest(A, B).val

        
        
        
        
        
        
        
        
        
        
        
        
        

