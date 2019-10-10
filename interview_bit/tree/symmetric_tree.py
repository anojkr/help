# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, r1, r2):
        if r1 == None and r2 == None:
            return 1
        elif r1 != None and r2 != None:
            return r1.val == r2.val and self.solve(r1.left,r2.right) and self.solve(r1.right ,r2.left)
        return 0
    def isSymmetric(self, A):
        test = self.solve(A.left, A.right)
        if test == 0:
            return 0
        return 1
