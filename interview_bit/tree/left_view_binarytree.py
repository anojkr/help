# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import defaultdict
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    
    def height(self, r):
        if r == None:
            return 0
        l = self.height(r.left)
        r = self.height(r.right)
        
        return 1 + max(l, r)
    
    def traverse(self, r, i, level, d):
        if r == None:
            return 
        if level == 1:
            d[i].append(r.val)
            return 
        else:
            self.traverse(r.left, i, level-1, d)
            self.traverse(r.right, i, level-1, d)
    
    def solve(self, A):
        r = A
        if r == None:
            return 
        h = self.height(r)
        d = defaultdict(list)
        for i in range(1, h+1):
            self.traverse(r, i, i, d)
            
        res  = []
        # print(d)
        for k, item in d.items():
            res.append(item[0])
        # return " ".join(map(str, res))
        return res
            
            
            
        
        
