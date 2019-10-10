# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    
    def solve(self, A, B, C):
        if A == None:
            return None
        
        if A.val == B or A.val == C:
            return A
        
        l = self.solve(A.left, B, C)
        r = self.solve(A.right, B, C)
        
        if l != None and r != None:
            return A
        
        if l == None:
            return r
        elif r == None:
            return l
        
    def lca(self, A, B, C):
        t = self.solve(A, B, C)
        if  t!= None:
            return t.val
        else:
            return -1

        
        # return A.val + t
        
        
        
        
        
        
        
        
        
        
        
        
        
        
