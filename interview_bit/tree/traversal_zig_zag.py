# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    
    def height(self, A):
        if A == None:
            return 0
            
        l = self.height(A.left)
        r = self.height(A.right)
        
        return 1 + max(l, r)
        
    def solve(self, A, level, ltr, res):
        
        if A == None:
            return
        
        if level == 1:
            res.append(A.val)
        
        if(ltr == 0):
            
            self.solve(A.left, level-1, ltr, res)
            self.solve(A.right, level-1, ltr, res)
            
        elif ltr == 1:
            # res.append(A.val)
            self.solve(A.right, level-1, ltr, res)
            self.solve(A.left, level-1, ltr, res)
        
    def zigzagLevelOrder(self, A):
        
        if A == None:
            return 
        
        h = self.height(A)
        result = []
        ltr = 0
        for i in range(1, h+1):
            res = []
            self.solve(A, i, ltr, res)
            ltr = abs(1-ltr)
            result.append(res)
        return result

