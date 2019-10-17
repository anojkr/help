# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer

    def traversal(self, r, res):
        if r == None:
            return 
        self.traversal(r.left, res)
        res.append(r.val)
        self.traversal(r.right, res)
        
    def isValidBST(self, A):
        res = []
        self.traversal(A, res)
        flag = 1 
        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                flag = 0
                break
        if flag == 0:
            return 0
        else:
            return 1
        
        
