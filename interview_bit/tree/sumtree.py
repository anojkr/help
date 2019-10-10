# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    def sum(self, root):
        if root == None:
            return 0
        return self.sum(root.left) + root.val + self.sum(root.right)
        
    def sumtree(self, A):
        if A == None:
            return 1
        if A.left == None and A.right == None:
            return 1
            
        l_s = self.sum(A.left)
        r_s = self.sum(A.right)
        if l_s + r_s == A.val:
            return (self.solve(A.left) and self.solve(A.right))
        return 0
        
    def solve(self, A):
        t = self.sumtree(A)
        if t == 0:
            return 0
        else:
            return 1
        

