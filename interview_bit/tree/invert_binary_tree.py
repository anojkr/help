# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    
    def invert(self, A):
        if A == None:
            return
        self.invert(A.left)
        self.invert(A.right)
        t = A.left
        A.left =A.right
        A.right = t

    def invertTree(self, A):
        if A == None:
            return
        
        self.invert(A)
        return A

