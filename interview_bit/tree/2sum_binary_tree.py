# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    
    def solve(self, A, B, d):
        if A == None:
            return 
            
        d[A.val] = 1
        self.solve(A.left, B, d)
        self.solve(A.right, B, d)
    
    def t2Sum(self, A, B):
        if A == None:
            return
        d = {}
        flag = 0
        self.solve(A, B, d)

        for k, item in d.items():
            d[k] = 2
            sub = B-k
            if sub in d and d[sub] !=2:
                flag = 1
                break
            d[k] = 1
        if flag == 1:
            return 1
        return 0
