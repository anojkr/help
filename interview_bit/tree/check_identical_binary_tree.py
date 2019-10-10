# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    
    def solve(self, A, B):
        if A == None and B == None:
            return 1
            
        if A!= None and B!= None:
            return (A.val == B.val and self.solve(A.left, B.left) and self.solve(A.right, B.right))
        return 0
        
    def isSameTree(self, A, B):
        
        if A == None and B == None:
            return 1
        
        x = self.solve(A, B)
        if x == 0:
            return 0
        return 1
