# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    res = []
    def pre(self, root):
        if root == None:
            return
        if root.left != None:
            self.res.append(root.val)
            self.pre(root.left)
        elif root.right != None:
            self.res.append(root.val)
            self.pre(root.right)
            
        
    def post(self, root):
        if root == None:
            return
        if root.right != None:
            self.post(root.right)
            self.res.append(root.val)
        elif root.left != None:
            self.post(root.left)
            self.res.append(root.val)
        
    def leave(self, root):
        if root == None:
            return
        self.leave(root.left)
        if root.left == None and root.right == None:
            self.res.append(root.val)
        self.leave(root.right)
        
    def solve(self, A):
        self.res = []
        if A != None:
            self.res.append(A.val)
            self.pre(A.left)
            self.leave(A.left)
            self.leave(A.right)
            self.post(A.right)
        return self.res
        
        
        
        
        
        
        
        
        
        
        
        
