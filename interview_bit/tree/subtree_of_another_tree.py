# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def identical(self, r, s):
        if r == None and s == None:
            return 1
        elif r == None or s == None:
            return 0
        elif r!= None and s!= None:
            return (r.val == s.val and self.identical(r.left, s.left) and self.identical(r.right, s.right))
    
        # return 0
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s ==  None:
            return 0
        if t == None:
            return 1
        
        if self.identical(s, t):
            return 1
    
        return self.identical(s.left, t) or self.identical(s.right, t)